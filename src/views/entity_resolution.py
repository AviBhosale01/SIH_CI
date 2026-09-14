"""
CrimeLens - Unified Entity Extraction & Resolution Module
Displays extracted entities across heterogeneous records and provides an interactive
entity resolution / deduplication workspace (USP 2).
"""
import streamlit as st
import pandas as pd
from src.core.synthetic_data import DEMO_ENTITIES, DEMO_DUPLICATES

def render_entity_resolution_view():
    """
    Render unified Entity Extraction & Resolution interface on a single page,
    demonstrating candidate matching, fuzzy phonetic scoring, and entity unification.
    """
    st.markdown("## 🧬 Entity Extraction & Resolution")
    st.write("Automatically extracted named entities from FIRs, CDRs, and vehicle registries, combined with CrimeLens's **Entity Resolution Engine** to detect duplicate identities across fragmented police logs.")

    # 1. TOP SECTION: EXTRACTED ENTITIES DIRECTORY
    st.markdown("### 📋 Extracted Named Entities (Across Ingested Records)")

    col_filter1, col_filter2 = st.columns([1.5, 2])
    with col_filter1:
        type_options = ["ALL TYPES", "PERSON", "VEHICLE", "PHONE", "LOCATION", "TRANSACTION"]
        selected_type = st.selectbox("Filter Entity Classification", type_options)
    with col_filter2:
        search_kw = st.text_input("Search Extracted Name / ID", placeholder="e.g. Rahul, MH12, Swift, Paud Road...")

    # Build display table from DEMO_ENTITIES
    table_rows = []
    for e in DEMO_ENTITIES:
        if selected_type != "ALL TYPES" and e["type"] != selected_type:
            continue
        if search_kw and search_kw.lower() not in e["name"].lower() and search_kw.lower() not in e["id"].lower():
            continue

        table_rows.append({
            "Entity ID": e["id"],
            "Entity Name / Label": e["name"],
            "Classification": e["type"],
            "Primary Linked Case": e["cases"][0] if e["cases"] else "N/A",
            "Cross-Case Presence": ", ".join(e["cases"]),
            "Extraction Confidence": "98% (High)" if e["type"] in ["PERSON", "PHONE"] else "100% (Exact)"
        })

    df_entities_display = pd.DataFrame(table_rows)
    st.dataframe(df_entities_display, use_container_width=True, hide_index=True)

    st.markdown("<br><hr style='border-top: 1px solid rgba(0, 229, 255, 0.25); margin: 20px 0;'>", unsafe_allow_html=True)

    # 2. BOTTOM SECTION: ENTITY RESOLUTION & DEDUPLICATION (USP 2)
    st.markdown("### 🔍 Entity Resolution & Discrepancy Matching (USP 02)")
    st.write("Different records often record misspelled names or shortened aliases for the same underlying subject. The resolution engine calculates candidate match scores and offers 1-click unification:")

    if "resolution_status" not in st.session_state:
        st.session_state["resolution_status"] = "PENDING"

    for dup in DEMO_DUPLICATES:
        status = st.session_state["resolution_status"]

        status_badge = (
            "<span style='background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; padding: 4px 12px; border-radius: 6px; font-weight: 800;'>✅ UNIFIED UNDER ENT-001</span>"
            if status == "CONFIRMED" else
            "<span style='background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; padding: 4px 12px; border-radius: 6px; font-weight: 800;'>⚠️ MATCH CANDIDATE PENDING REVIEW</span>"
        )

        st.markdown(f"""
        <div style="background: rgba(13, 21, 39, 0.90); border: 1px solid rgba(0, 229, 255, 0.35); border-radius: 14px; padding: 22px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 3px 10px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">{dup['candidate_id']}</span>
                    <h3 style="margin: 0; color: #ffffff; font-size: 1.3rem;">Potential Entity Duplicate Detected</h3>
                </div>
                {status_badge}
            </div>

            <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;">
                Multiple evidence streams recorded closely matched biographical and physical indicators for the primary subject:
            </p>

            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 18px;">
                <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                    <span style="background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">RECORD A — {dup['record_a']['source']}</span>
                    <h4 style="margin: 8px 0 4px 0; color: #ffffff;">{dup['record_a']['raw_name']}</h4>
                    <div style="font-size: 0.8rem; color: #cbd5e1;">
                        📱 {dup['record_a']['phone']}<br>
                        🚗 {dup['record_a']['vehicle']}<br>
                        📍 {dup['record_a']['location']}
                    </div>
                </div>
                <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                    <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">RECORD B — {dup['record_b']['source']}</span>
                    <h4 style="margin: 8px 0 4px 0; color: #ffffff;">{dup['record_b']['raw_name']}</h4>
                    <div style="font-size: 0.8rem; color: #cbd5e1;">
                        📱 {dup['record_b']['phone']}<br>
                        🚗 {dup['record_b']['vehicle']}<br>
                        📍 {dup['record_b']['location']}
                    </div>
                </div>
                <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                    <span style="background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">RECORD C — {dup['record_c']['source']}</span>
                    <h4 style="margin: 8px 0 4px 0; color: #ffffff;">{dup['record_c']['raw_name']}</h4>
                    <div style="font-size: 0.8rem; color: #cbd5e1;">
                        📱 {dup['record_c']['phone']}<br>
                        🚗 {dup['record_c']['vehicle']}<br>
                        📍 {dup['record_c']['location']}
                    </div>
                </div>
            </div>

            <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 8px; padding: 14px; margin-bottom: 18px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <b style="color: #00e5ff;">Composite Match Confidence:</b>
                    <span style="font-size: 1.3rem; font-weight: 800; color: #34d399; font-family: 'JetBrains Mono', monospace;">{dup['match_score']}% MATCH</span>
                </div>
                <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
                    ✓ <b>Phonetic &amp; Levenshtein Similarity</b>: 94% string proximity between <i>Rahul Sharma</i> and <i>Rahul Sharm</i>.<br>
                    ✓ <b>Exact Telecommunication Identifier</b>: Exact MSISDN match (+91 98765 43210) across FIR and CDR logs.<br>
                    ✓ <b>Shared Asset Ownership</b>: Same license plate MH12AB1234 registered under RTO identity <i>Rahul S.</i><br>
                    ✓ <b>Spatial Co-location</b>: Overlapping presence within Kothrud sector jurisdiction.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_act1, col_act2, _ = st.columns([1.8, 1.5, 4])
        with col_act1:
            if st.button("✅ Confirm Match & Merge Entities", key="btn_confirm_merge", use_container_width=True):
                st.session_state["resolution_status"] = "CONFIRMED"
                st.success(f"Entities confirmed! Successfully unified under Unified Entity ID: ENT-001 (Rahul Sharma).")
                st.rerun()
        with col_act2:
            if st.button("❌ Reject Discrepancy", key="btn_reject_merge", use_container_width=True):
                st.session_state["resolution_status"] = "REJECTED"
                st.info("Records marked as distinct entities.")
                st.rerun()

        if status == "CONFIRMED":
            st.markdown("""
            <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid #10b981; border-radius: 8px; padding: 14px; margin-top: 10px;">
                <b style="color: #34d399;">Unified Entity State:</b><br>
                All references in Case <b>FIR-104</b>, <b>FIR-087</b>, and CDR logs are now mapped to 
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 800; color: #00e5ff;">ENT-001 [Rahul Sharma]</span>. 
                Investigation Knowledge Graph automatically synchronizes edges.
            </div>
            """, unsafe_allow_html=True)
