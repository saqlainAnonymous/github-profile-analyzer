import unittest
from unittest.mock import Mock
from github_analyzer import GitHubAnalyzer, GitHubAPIError

class AnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.session=Mock()
        self.analyzer=GitHubAnalyzer(session=self.session)

    def test_analysis_aggregates_data(self):
        profile={'login':'octocat','name':'Octocat','public_repos':2,'followers':10,'following':3}
        repos=[{'name':'alpha','stargazers_count':5,'forks_count':2,'language':'Python','html_url':'https://github.com/octocat/alpha'},{'name':'beta','stargazers_count':2,'forks_count':1,'language':'Python','html_url':'https://github.com/octocat/beta'}]
        events=[{'type':'PushEvent','repo':{'name':'octocat/alpha'},'created_at':'2025-01-01','payload':{'ref_type':'branch'}}]
        self.session.get.side_effect=[Mock(status_code=200,ok=True,json=lambda:profile),Mock(status_code=200,ok=True,json=lambda:repos),Mock(status_code=200,ok=True,json=lambda:events)]
        result=self.analyzer.analyze('octocat')
        self.assertEqual(result['total_stars'],7)
        self.assertEqual(result['total_forks'],3)
        self.assertEqual(result['languages'],{'Python':2})
        self.assertEqual(result['top_repositories'][0]['name'],'alpha')

    def test_empty_username(self):
        with self.assertRaises(ValueError): self.analyzer.analyze(' ')

    def test_not_found(self):
        self.session.get.return_value=Mock(status_code=404,ok=False,text='Not Found',headers={})
        with self.assertRaisesRegex(GitHubAPIError,'not found'): self.analyzer.analyze('missing')

    def test_rate_limit(self):
        self.session.get.return_value=Mock(status_code=403,ok=False,text='rate limit',headers={'X-RateLimit-Remaining':'0'})
        with self.assertRaisesRegex(GitHubAPIError,'rate limit'): self.analyzer.analyze('octocat')

if __name__ == '__main__': unittest.main()
