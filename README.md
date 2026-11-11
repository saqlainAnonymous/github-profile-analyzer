# GitHub Profile Analyzer

A Streamlit dashboard for public GitHub profile analytics.

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

## Deploy online (free)
1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Sign in with the GitHub account that can access this public repository.
3. Select **Create app** and choose:
   - Repository: `saqlainAnonymous/github-profile-analyzer`
   - Branch: `main`
   - Main file path: `app.py`
4. Select **Deploy**. Streamlit installs the packages from `requirements.txt` automatically.
5. After the app finishes building, copy its public URL and add it to this README.

You can also use the **Open in Streamlit** badge above to start the deployment flow.

## Tests
```bash
python -m pytest -q
```

## Limitations
Only public data is included. This version fetches up to 100 owned repositories. Language distribution counts each repository's primary language, not bytes of code.

## License
MIT.
