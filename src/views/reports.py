"""
CrimeLens - Investigation Report Generator Module
Compiles structured police intelligence dossiers, cross-case summaries,
and downloadable formal investigation reports.
"""
import streamlit as st
from datetime import datetime
from src.core.synthetic_data import DEMO_CASES, DEMO_PRIORITY_LEADS, DEMO_CROSS_CASE_INSIGHTS
from src.utils.styles import render_html

def generate_report_text(case_id: str, investigator_name: str, badge_id: str):
    """Generate structured police intelligence report markdown string."""
    case_meta = next((c for c in DEMO_CASES if c["case_id"] == case_id), DEMO_CASES[0])
    date_now = datetime.now().strftime("%d %B %Y, %I:%M %p IST")

    report_lines = [
        "=" * 70,
        "CRIMELENS POLICE INTELLIGENCE & INVESTIGATION REPORT",
        "CONFIDENTIAL — LAW ENFORCEMENT OPERATIONAL BRIEFING",
        "=" * 70,
        f"REPORT TIMESTAMP   : {date_now}",
        f"CASE IDENTIFIER    : {case_meta['case_id']}",
        f"CRIME TITLE        : {case_meta['title']}",
        f"POLICE STATION     : {case_meta['station']}",
        f"INVESTIGATING OFF. : {investigator_name} ({badge_id})",
        f"STATUS / PRIORITY  : {case_meta['status']} / {case_meta['priority']}",
        "-" * 70,
        "",
        "1. EXECUTIVE INCIDENT OVERVIEW:",
        f"   {case_meta['description']}",
        f"   Incident Location: {case_meta['location']}",
        f"   Registration Date: {case_meta['date']}",
        "",
        "2. PRIMARY PERSONS OF INTEREST & ASSETS (TOP LEADS):",
    ]

    for lead in DEMO_PRIORITY_LEADS:
        report_lines.extend([
            f"   • {lead['name']} ({lead['type']}) — PRIORITY SCORE: {lead['score']}/100 [{lead['level']}]",
            f"     Reason: {', '.join(lead['reasons'])}",
            f"     Underlying Evidence: {', '.join(lead['evidence'])}"
        ])

    report_lines.extend([
        "",
        "3. CROSS-CASE EVIDENCE DISCOVERIES:",
    ])

    for ins in DEMO_CROSS_CASE_INSIGHTS:
        report_lines.extend([
            f"   • [{ins['insight_id']}] {ins['title']} ({ins['severity']})",
            f"     Summary: {ins['summary']}",
            f"     Cases Linked: {', '.join(ins['cases_involved'])}",
            f"     Evidence Sources: {', '.join(ins['evidence_sources'])}"
        ])

    report_lines.extend([
        "",
        "4. 72-HOUR OPERATIONAL EVENT SEQUENCE:",
        "   • 10 Aug 23:45 IST: Getaway vehicle MH12AB1234 sighted exiting Swargate warehouse (FIR-087).",
        "   • 11 Aug 18:30 IST: 14 CDR calls logged between Rahul Sharma and Amit Verma.",
        "   • 12 Aug 09:15 IST: FIR-104 formally lodged at Kothrud PS.",
        "   • 13 Aug 14:22 IST: ₹75,000 IMPS fund transfer executed to accomplice Amit Verma (TXN-203).",
        "",
        "5. STATUTORY ADVISORY & DIRECTIVE:",
        "   • Priority scores and link graphs serve strictly as investigative triage heuristics.",
        "   • Formal warrants recommended for vehicle MH12AB1234 and interrogation of prime subjects.",
        "",
        "=" * 70,
        "END OF CRIMELENS INTELLIGENCE DOSSIER",
        "=" * 70
    ])

    return "\n".join(report_lines)


def render_reports_view():
    """
    Render Investigation Report Generator with case selector,
    formatted dossier preview, and downloadable report document.
    """
    st.markdown("## 📄 Investigation Report Generator")
    st.write("Compile structured, evidence-backed police intelligence dossiers suitable for supervisory submission and court filings.")

    active_case_id = st.session_state.get("active_case_id", "FIR-104")
    user = st.session_state.get("authenticated_user", {})
    user_name = user.get("name", "PI Vikram Patil")
    badge_id = user.get("badge_id", "MH-PN-4082")

    col_c1, col_c2 = st.columns([2, 1.5])
    with col_c1:
        selected_rep_case = st.selectbox(
            "Select Case for Dossier Compilation",
            [c["case_id"] for c in DEMO_CASES],
            index=0 if active_case_id not in [c["case_id"] for c in DEMO_CASES] else [c["case_id"] for c in DEMO_CASES].index(active_case_id)
        )
    with col_c2:
        render_html("<div style='padding-top: 28px;'></div>")
        generate_btn = st.button("⚡ Compile Structured Intelligence Report", key="btn_gen_report", use_container_width=True)

    report_content = generate_report_text(selected_rep_case, user_name, badge_id)

    st.markdown("### 📋 Generated Intelligence Dossier Preview")
    st.code(report_content, language="text")

    # Download Buttons
    down_col1, down_col2, _ = st.columns([1.5, 1.5, 3])
    with down_col1:
        st.download_button(
            "📥 Download Report (.TXT)",
            data=report_content,
            file_name=f"CrimeLens_Report_{selected_rep_case}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with down_col2:
        st.download_button(
            "📄 Export Dossier (.MD)",
            data=f"```text\n{report_content}\n```",
            file_name=f"CrimeLens_Dossier_{selected_rep_case}.md",
            mime="text/markdown",
            use_container_width=True
        )
