# GitHub Profile Analyzer

A Streamlit dashboard for public GitHub profile analytics.

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

## Tests
```bash
python -m pytest -q
```

## Limitations
Only public data is included. This version fetches up to 100 owned repositories. Language distribution counts each repository's primary language, not bytes of code.

## License
MIT.