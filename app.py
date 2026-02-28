import streamlit as st
from agents.domain_detector import detect_domain
from agents.decision_planner import plan_decision
from agents.synthesis_agent import generate_report
from agents.critic_agent import critique_and_improve


st.set_page_config(page_title="OMNIS Decision Intelligence", layout="wide")

st.title("🧠 OMNIS — Multi-Agent Intelligence System")

st.markdown("Ask any strategic decision question and receive structured AI analysis.")

user_query = st.text_area("Enter your decision question:", height=120)

if st.button("Analyze Decision"):

    if not user_query.strip():
        st.warning("Please enter a decision question.")
    else:
        with st.spinner("Running multi-agent analysis..."):

            # Domain Detection
            domain = detect_domain(user_query)

            # Planning
            plan = plan_decision(user_query, domain)

            # Final Report
            report = generate_report(user_query, domain, plan)

            # Critique
            critique = critique_and_improve(user_query, domain, plan, report)

        st.subheader("🔍 Detected Domain")
        st.success(domain)

        st.subheader("📊 Decision Planning Analysis")
        st.write(plan)

        st.subheader("📝 Final Recommendation")
        st.markdown(report)

        st.subheader("🧠 Self-Critique & Confidence")
        st.write(critique)


st.markdown("---")
st.caption("OMNIS v1.0 — Multi-Model Decision Architecture")