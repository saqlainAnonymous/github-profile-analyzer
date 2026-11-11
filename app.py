"""Streamlit dashboard for GitHub Profile Analyzer."""
import streamlit as st
from github_analyzer import GitHubAnalyzer, GitHubAPIError

st.set_page_config(page_title="GitHub Profile Analyzer", page_icon="🔎", layout="wide")
st.title("🔎 GitHub Profile Analyzer")
st.caption("A data-driven snapshot of any public GitHub profile.")
with st.sidebar:
    st.header("Analyze a profile")
    username = st.text_input("GitHub username", placeholder="torvalds")
    token = st.text_input("Optional GitHub token", type="password", help="Raises API rate limits. Never share your token.")
    analyze = st.button("Analyze profile", type="primary", use_container_width=True)
if analyze:
    if not username.strip():
        st.warning("Enter a GitHub username.")
        st.stop()
    try:
        with st.spinner("Fetching public GitHub data..."):
            st.session_state["analysis"] = GitHubAnalyzer(token=token or None).analyze(username.strip())
    except GitHubAPIError as exc:
        st.error(str(exc))
        st.stop()
data = st.session_state.get("analysis")
if not data:
    st.info("Enter a GitHub username in the sidebar and select Analyze profile.")
    st.markdown("### What you'll get\n- Public profile overview\n- Repository, star and fork statistics\n- Most-starred repositories\n- Language distribution\n- Recent public activity")
    st.stop()
profile = data["profile"]
st.subheader(profile.get("name") or profile["login"])
if profile.get("bio"): st.write(profile["bio"])
st.markdown(f"[View GitHub profile](https://github.com/{profile['login']}) · {profile.get('location') or 'Location not specified'}")
cols = st.columns(4)
for col, label, value in zip(cols, ["Public repos", "Followers", "Following", "Total stars"], [profile["public_repos"], profile["followers"], profile["following"], data["total_stars"]]):
    col.metric(label, f"{value:,}")
left, right = st.columns(2)
with left:
    st.markdown("### Top repositories")
    st.dataframe(data["top_repositories"], use_container_width=True, hide_index=True)
with right:
    st.markdown("### Languages")
    if data["languages"]: st.bar_chart(data["languages"])
    else: st.write("No language data available.")
st.markdown("### Recent public activity")
if data["recent_activity"]: st.dataframe(data["recent_activity"], use_container_width=True, hide_index=True)
else: st.write("No recent public activity was returned.")
st.caption("Only public GitHub data is included.")
