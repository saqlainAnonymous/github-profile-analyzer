from collections import Counter
from typing import Any
import requests

API = 'https://api.github.com'

class GitHubAPIError(RuntimeError):
    pass

class GitHubAnalyzer:
    def __init__(self, token: str | None = None, timeout: int = 15, session=None):
        self.session = session or requests.Session()
        self.timeout = timeout
        self.session.headers.update({'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'github-profile-analyzer'})
        if token:
            self.session.headers['Authorization'] = f'Bearer {token}'

    def _get(self, path: str) -> Any:
        try:
            response = self.session.get(f'{API}{path}', timeout=self.timeout)
        except requests.RequestException as exc:
            raise GitHubAPIError(f'Network error contacting GitHub: {exc}') from exc
        if response.status_code == 404:
            raise GitHubAPIError('GitHub user or resource not found. Check the username.')
        if response.status_code == 403 and response.headers.get('X-RateLimit-Remaining') == '0':
            raise GitHubAPIError('GitHub API rate limit reached. Add a personal access token and retry.')
        if not response.ok:
            raise GitHubAPIError(f'GitHub API returned HTTP {response.status_code}: {response.text[:200]}')
        return response.json()

    def analyze(self, username: str) -> dict[str, Any]:
        if not username or not username.strip():
            raise ValueError('Username cannot be empty.')
        login = username.strip()
        profile = self._get(f'/users/{login}')
        repos = self._get(f'/users/{login}/repos?per_page=100&sort=updated&type=owner')
        events = self._get(f'/users/{login}/events/public?per_page=30')
        languages = Counter(r['language'] for r in repos if r.get('language'))
        top = sorted(repos, key=lambda r:r.get('stargazers_count',0), reverse=True)[:10]
        recent = [{'type':e.get('type','Event'),'repository':(e.get('repo') or {}).get('name',''),'created_at':e.get('created_at',''),'detail':(e.get('payload') or {}).get('action') or (e.get('payload') or {}).get('ref_type') or ''} for e in events[:10]]
        return {'profile':{k:profile.get(k) for k in ('login','name','bio','location','avatar_url','html_url','created_at','public_repos','followers','following')},'total_stars':sum(r.get('stargazers_count',0) for r in repos),'total_forks':sum(r.get('forks_count',0) for r in repos),'languages':dict(languages.most_common()),'top_repositories':[{'name':r['name'],'stars':r.get('stargazers_count',0),'forks':r.get('forks_count',0),'language':r.get('language') or '—','url':r.get('html_url','')} for r in top],'recent_activity':recent}
