from agents.domain_detector import detect_domain
from agents.decision_planner import plan_decision
from agents.synthesis_agent import generate_report
from agents.critic_agent import critique_and_improve


def main():

    print("\n🚀 OMNIS Multi-Model Decision System\n")

    user_query = input("Enter your decision question:\n")

    if not user_query.strip():
        print("❌ Empty input. Exiting.")
        return

    # -------------------------
    # 1️⃣ Domain Detection
    # -------------------------
    print("\n🔍 Detecting domain...")
    domain = detect_domain(user_query)

    if not domain or domain == "Unknown":
        print("⚠️ Could not detect domain. Exiting safely.")
        return

    print(f"✅ Domain: {domain}")

    # -------------------------
    # 2️⃣ Planning Stage
    # -------------------------
    print("\n🧠 Planning decision...")
    plan = plan_decision(user_query, domain)

    if not plan:
        print("⚠️ Planning failed. Exiting safely.")
        return

    print("\n📊 Planner Output:\n")
    print(plan)

    # -------------------------
    # 3️⃣ Final Synthesis
    # -------------------------
    print("\n📝 Generating final report...")
    report = generate_report(user_query, domain, plan)

    if not report:
        print("⚠️ Report generation failed.")
        return

    print("\n" + "=" * 50)
    print("🧠 OMNIS FINAL DECISION REPORT")
    print("=" * 50 + "\n")

    print("\n🔎 Critiquing and improving recommendation...")
    improved_report = critique_and_improve(user_query, domain, plan, report)

    print("\n" + "=" * 50)
    print("🧠 OMNIS FINAL REFINED DECISION REPORT")
    print("=" * 50 + "\n")

    print(improved_report)


if __name__ == "__main__":
    main()