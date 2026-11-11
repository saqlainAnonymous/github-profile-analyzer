# GitHub Profile Analyzer

A Streamlit dashboard for public GitHub profile analytics.

<https://saqlainanonymous-github-profile-analyzer-app-oa9xzl.streamlit.app/>

[![Open Live App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://saqlainanonymous-github-profile-analyzer-app-oa9xzl.streamlit.app/)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=saqlainAnonymous%2Fgithub-profile-analyzer&branch=main&mainModule=app.py)

## Features
- Profile overview, followers and following
- Repository, star and fork totals
- Top repositories ranked by stars
- Primary-language distribution
- Recent public events
- Optional GitHub token for higher API rate limits
- Unit tests and GitHub Actions CI

## Run locally
Requires Python 3.10+.

```bash
git clone https://github.com/saqlainAnonymous/github-profile-analyzer.git
cd github-profile-analyzer
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
The app is deployed on Streamlit Community Cloud:

**Live app:** https://saqlainanonymous-github-profile-analyzer-app-oa9xzl.streamlit.app/

To redeploy or manage the app, open [Streamlit Community Cloud](https://share.streamlit.io/), sign in with the GitHub account that owns the repository, and select:
- Repository: `saqlainAnonymous/github-profile-analyzer`
- Branch: `main`
- Main file path: `app.py`

## Tests
```bash
python -m pytest -q
```

## Limitations
Only public data is included. This version fetches up to 100 owned repositories. Language distribution counts each repository's primary language, not bytes of code.

## License
MIT.
