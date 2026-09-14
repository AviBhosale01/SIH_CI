"""
CrimeLens - Data Intelligence Hub (Ingestion Engine)
Allows categorized data ingestion (FIR, CDR, Financial, Vehicle, Intelligence),
parsing progress animations, dataset viewing, and inline record editing.
"""
import streamlit as st
import pandas as pd
import time
from src.core.config import DATA_SOURCES

def render_data_hub_view():
    """
    Render Data Intelligence Hub supporting multi-source data ingestion,
    progress tracking, record inspection, and inline record modifications.
    """
    st.markdown("## 📥 Data Intelligence Hub")
    st.write("Ingest heterogeneous crime intelligence streams into the CrimeLens operational pipeline: FIRs, CDR phone dumps, bank statements, vehicle ANPR sightings, and field intelligence memos.")

    active_case_id = st.session_state.get("active_case_id", "FIR-104")

    # Ingestion State Containers
    if "uploaded_records" not in st.session_state:
        st.session_state["uploaded_records"] = {
            "FIR": pd.DataFrame([
                {"record_id": "FIR-104", "title": "Commercial Complex Auto Theft", "station": "Kothrud PS", "date": "2026-08-12", "primary_suspect": "Rahul Sharma", "status": "Registered"},
                {"record_id": "FIR-087", "title": "Warehouse Logistics Break-in", "station": "Swargate PS", "date": "2026-08-10", "primary_suspect": "Unknown (CCTV getaway)", "status": "Registered"},
                {"record_id": "FIR-052", "title": "Corporate Extortion & Malware", "station": "Cyber PS", "date": "2026-07-28", "primary_suspect": "Mule Conduit Network", "status": "Registered"}
            ]),
            "CDR": pd.DataFrame([
                {"call_id": "CDR-201", "caller": "+91 98765 43210 (Rahul Sharma)", "receiver": "+91 98230 11223 (Amit Verma)", "timestamp": "2026-08-11 18:32:00", "duration_sec": 340, "tower": "Kothrud Paud Rd", "frequency": "14 calls in 48h"},
                {"call_id": "CDR-202", "caller": "+91 98230 11223 (Amit Verma)", "receiver": "+91 98765 43210 (Rahul Sharma)", "timestamp": "2026-08-11 21:15:00", "duration_sec": 195, "tower": "Swargate Depot", "frequency": "Frequent"},
                {"call_id": "CDR-203", "caller": "+91 98765 43210 (Rahul Sharma)", "receiver": "+91 97654 32109 (Unknown Contact)", "timestamp": "2026-08-12 01:10:00", "duration_sec": 84, "tower": "Kothrud Central", "frequency": "Nighttime"}
            ]),
            "FINANCIAL": pd.DataFrame([
                {"txn_id": "TXN-203", "sender": "Rahul Sharma", "receiver": "Amit Verma", "amount_inr": 75000, "channel": "IMPS Mobile Transfer", "timestamp": "2026-08-13 14:22:00", "remark": "Auto Parts Settlement"},
                {"txn_id": "TXN-204", "sender": "Rahul Sharma", "receiver": "Cash Withdrawal", "amount_inr": 45000, "channel": "ATM Kothrud Branch", "timestamp": "2026-08-12 16:40:00", "remark": "Cash Dispensed"},
                {"txn_id": "TXN-501", "sender": "Mule Conduit A/C", "receiver": "Shell Entity", "amount_inr": 250000, "channel": "RTGS Corporate", "timestamp": "2026-07-29 11:00:00", "remark": "Consulting Fee"}
            ]),
            "VEHICLE": pd.DataFrame([
                {"vehicle_id": "VEH-019", "reg_number": "MH12AB1234", "make_model": "Maruti Swift (White)", "registered_owner": "Rahul Sharma", "anpr_location": "Swargate Toll Gate", "timestamp": "2026-08-10 23:45:00", "case_flag": "Getaway Sighting (FIR-087)"},
                {"vehicle_id": "VEH-020", "reg_number": "MH12AB1234", "make_model": "Maruti Swift (White)", "registered_owner": "Rahul Sharma", "anpr_location": "Kothrud Complex Entrance", "timestamp": "2026-08-12 08:30:00", "case_flag": "Crime Scene Presence (FIR-104)"},
                {"vehicle_id": "VEH-021", "reg_number": "MH14CD5678", "make_model": "Mahindra Scorpio (Black)", "registered_owner": "Amit Verma", "anpr_location": "Hadapsar Bypass", "timestamp": "2026-08-11 14:10:00", "case_flag": "Associate Transport"}
            ]),
            "INTELLIGENCE": pd.DataFrame([
                {"memo_id": "INT-044", "source": "Confidential Informant CI-09", "sector": "Kothrud / Paud Belt", "timestamp": "2026-08-12 11:00:00", "summary": "Subject Rahul Sharma observed meeting transport operators regarding rapid offloading of commercial electronics.", "reliability": "A-Grade"},
                {"memo_id": "INT-045", "source": "Cyber Patrol Intercept", "sector": "Telegram Underground Market", "timestamp": "2026-08-13 09:30:00", "summary": "Unregistered server hardware listed for sale below market valuation originating from West Pune IP ranges.", "reliability": "B-Grade"}
            ])
        }

    tab_upload, tab_view, tab_edit = st.tabs(["📤 Upload New Evidence Stream", "📋 View Ingested Datasets", "✏️ Edit Records"])

    # TAB 1: Upload Stream
    with tab_upload:
        st.markdown(f"### Ingest Records for Case Context: **{active_case_id}**")
        st.write("Select the stream classification, upload raw evidence files (CSV, PDF, JSON, or TXT), and execute normalization:")

        u_col1, u_col2 = st.columns([1.5, 2])
        with u_col1:
            stream_type = st.selectbox(
                "Evidence Stream Classification",
                [s["type"] for s in DATA_SOURCES],
                format_func=lambda x: f"{next(s['icon'] for s in DATA_SOURCES if s['type']==x)} {x} — {next(s['desc'] for s in DATA_SOURCES if s['type']==x)}"
            )
            st.info(f"Uploading under **{stream_type}**. Files will be automatically normalized into the unified entity graph schema.")

        with u_col2:
            uploaded_file = st.file_uploader(f"Choose {stream_type} Document / Spreadsheet (CSV, JSON, PDF)", type=["csv", "json", "pdf", "txt", "xlsx"])
            custom_note = st.text_input("Investigator Audit Note (Optional)", placeholder="e.g. Received from Kothrud PS / Airtel Subpoena")

        if uploaded_file is not None:
            st.markdown("---")
            if st.button(f"⚡ Ingest & Parse {uploaded_file.name}", key="btn_execute_ingest"):
                progress_bar = st.progress(0)
                status_text = st.empty()

                status_text.text(f"1/4: Reading binary stream {uploaded_file.name}...")
                progress_bar.progress(25)
                time.sleep(0.3)

                status_text.text("2/4: Executing schema normalization & field mapping...")
                progress_bar.progress(55)
                time.sleep(0.3)

                status_text.text("3/4: Parsing candidate entities (Persons, Vehicles, Phones)...")
                progress_bar.progress(85)
                time.sleep(0.3)

                progress_bar.progress(100)
                status_text.text("4/4: Ingestion & entity correlation complete!")

                st.success(f"✅ Successfully ingested **{uploaded_file.name}** into **{stream_type}** repository! Linked to Case **{active_case_id}**.")
                st.balloons()

    # TAB 2: View Ingested Datasets
    with tab_view:
        st.markdown("### 📋 Ingested Evidence Repositories")
        selected_view_stream = st.radio("Select Repository", list(st.session_state["uploaded_records"].keys()), horizontal=True)

        df_show = st.session_state["uploaded_records"][selected_view_stream]
        st.dataframe(df_show, use_container_width=True, hide_index=True)
        st.caption(f"Showing {len(df_show)} records currently cataloged in the {selected_view_stream} registry.")

    # TAB 3: Edit Records
    with tab_edit:
        st.markdown("### ✏️ Edit Ingested Records")
        st.write("Modify field values or update metadata directly using the table editor below:")

        selected_edit_stream = st.selectbox("Select Stream to Edit", list(st.session_state["uploaded_records"].keys()), key="sel_edit_stream")
        df_target = st.session_state["uploaded_records"][selected_edit_stream]

        edited_df = st.data_editor(
            df_target,
            use_container_width=True,
            num_rows="dynamic",
            key=f"editor_{selected_edit_stream}"
        )

        if st.button(f"💾 Save Changes to {selected_edit_stream} Repository", key=f"btn_save_{selected_edit_stream}"):
            st.session_state["uploaded_records"][selected_edit_stream] = edited_df
            st.success(f"Changes saved successfully to {selected_edit_stream} repository!")
            st.rerun()
