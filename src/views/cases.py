"""
CrimeLens - Case Management View Module
Handles case dossier browsing, investigation overview stats, and new FIR case registration.
"""
import streamlit as st
from src.core.synthetic_data import DEMO_CASES
from src.utils.styles import render_html

def render_cases_view():
    """
    Render Case Management explorer with case overview, status filters,
    and new case registration dialog.
    """
    st.markdown("## 📁 Case Management Dossier")
    st.write("Browse ongoing police investigations, inspect active evidence counts, or register a new FIR case file.")

    active_case_id = st.session_state.get("active_case_id", "FIR-104")

    # Tab 1: Case Explorer, Tab 2: Create New Case
    tab_list, tab_create = st.tabs(["📂 Active Case Dossiers", "➕ Register New Case"])

    with tab_list:
        col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
        with col_f1:
            search_case = st.text_input("🔍 Search Case ID, Title, or Officer", placeholder="e.g. FIR-104, Theft, Vikram Patil...")
        with col_f2:
            status_filter = st.selectbox("Filter Status", ["All Statuses", "ACTIVE", "IN REVIEW", "CLOSED"])
        with col_f3:
            priority_filter = st.selectbox("Filter Priority", ["All Priorities", "HIGH", "MEDIUM", "LOW"])

        filtered_cases = [c for c in DEMO_CASES]
        if search_case:
            filtered_cases = [c for c in filtered_cases if search_case.lower() in c["case_id"].lower() or search_case.lower() in c["title"].lower() or search_case.lower() in c["io_name"].lower()]
        if status_filter != "All Statuses":
            filtered_cases = [c for c in filtered_cases if c["status"] == status_filter]
        if priority_filter != "All Priorities":
            filtered_cases = [c for c in filtered_cases if c["priority"] == priority_filter]

        st.markdown(f"Found **{len(filtered_cases)}** investigation files.")

        for c in filtered_cases:
            is_active = (c["case_id"] == active_case_id)
            border_color = "rgba(0, 229, 255, 0.7)" if is_active else "rgba(75, 85, 99, 0.35)"
            bg_color = "rgba(0, 229, 255, 0.05)" if is_active else "rgba(15, 23, 42, 0.8)"
            badge_color = "#ef4444" if c["priority"] == "HIGH" else "#f59e0b"

            with st.container():
                render_html(f"""
                <div style="background: {bg_color}; border: 1px solid {border_color}; border-radius: 12px; padding: 18px; margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #00e5ff; font-weight: 800; font-family: 'JetBrains Mono', monospace; font-size: 1.15rem;">{c['case_id']}</span>
                            <span style="background: {badge_color}22; color: {badge_color}; border: 1px solid {badge_color}; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">{c['priority']} PRIORITY</span>
                            <span style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid #10b981; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">{c['status']}</span>
                        </div>
                        <span style="color: #94a3b8; font-size: 0.85rem;">📅 Registered: <b>{c['date']}</b></span>
                    </div>
                    <h3 style="margin: 4px 0 8px 0; font-size: 1.25rem; color: #ffffff;">{c['title']}</h3>
                    <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5; margin-bottom: 14px;">{c['description']}</p>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; text-align: center; font-size: 0.85rem;">
                        <div><span style="color: #94a3b8;">Location:</span><br><b style="color: #ffffff;">{c['location']}</b></div>
                        <div><span style="color: #94a3b8;">Investigating Officer:</span><br><b style="color: #ffffff;">{c['io_name']}</b></div>
                        <div><span style="color: #94a3b8;">Connected Entities:</span><br><b style="color: #00e5ff;">{c['entities_count']}</b></div>
                        <div><span style="color: #94a3b8;">Evidence Items:</span><br><b style="color: #34d399;">{c['evidence_count']}</b></div>
                    </div>
                </div>
                """)

                col_btn1, col_btn2, _ = st.columns([1.5, 2, 4])
                with col_btn1:
                    if st.button("Set as Active Case", key=f"btn_set_active_{c['case_id']}", use_container_width=True):
                        st.session_state["active_case_id"] = c["case_id"]
                        st.success(f"Case {c['case_id']} is now set as the active working context!")
                        st.rerun()
                with col_btn2:
                    if st.button("🕸️ Build Investigation Graph", key=f"btn_graph_case_{c['case_id']}", use_container_width=True):
                        st.session_state["active_case_id"] = c["case_id"]
                        st.session_state["nav_route"] = "🕸️ Knowledge Graph Workspace"
                        st.rerun()

    with tab_create:
        st.markdown("### ➕ Lodge / Register New Investigation Case")
        st.write("Register a new FIR incident to initialize entity mapping and evidence correlation:")

        with st.form("form_create_new_case", clear_on_submit=True):
            col_nc1, col_nc2 = st.columns(2)
            with col_nc1:
                new_case_id = st.text_input("FIR / Case Registration Number", value=f"FIR-0{len(DEMO_CASES)+1}5", placeholder="e.g. FIR-112")
                new_title = st.text_input("Investigation Title / Crime Summary", placeholder="e.g. Organised Gold Smuggling & Hawala Conduit")
                new_location = st.text_input("Incident Location / Sector", placeholder="e.g. Deccan Gymkhana, Pune")
            with col_nc2:
                new_priority = st.selectbox("Priority Assessment", ["HIGH", "MEDIUM", "LOW"])
                new_station = st.selectbox("Police Station Jurisdiction", [
                    "Kothrud Police Station",
                    "Swargate Police Station",
                    "Shivajinagar Police Station",
                    "Hinjawadi Cyber Police Station",
                    "Crime Branch Unit 1"
                ])
                new_io = st.text_input("Assigned Investigating Officer (IO)", value="PI Vikram Patil (MH-PN-4082)")

            new_desc = st.text_area("Initial Case Narrative / Incident Details", placeholder="Detailed overview of offense reported, primary complainants, and initial leads...")

            submit_case = st.form_submit_button("Register Case Dossier")

            if submit_case:
                if not new_case_id or not new_title:
                    st.error("Case ID and Title are mandatory fields.")
                else:
                    new_case_obj = {
                        "case_id": new_case_id,
                        "title": new_title,
                        "date": "2026-08-14",
                        "location": new_location,
                        "station": new_station,
                        "io_name": new_io.split("(")[0].strip(),
                        "io_badge": "MH-PN-4082",
                        "status": "ACTIVE",
                        "priority": new_priority,
                        "description": new_desc,
                        "entities_count": 0,
                        "relations_count": 0,
                        "evidence_count": 1,
                        "alerts_count": 0
                    }
                    DEMO_CASES.append(new_case_obj)
                    st.session_state["active_case_id"] = new_case_id
                    st.success(f"Case {new_case_id} registered successfully! Set as active working context.")
                    st.rerun()
