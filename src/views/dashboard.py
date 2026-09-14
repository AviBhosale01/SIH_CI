"""
CrimeLens - Investigator Dashboard View Module
Primary command center displaying active case intelligence metrics, recent FIR files,
and urgent investigative leads.
"""
import streamlit as st
import pandas as pd
from src.core.synthetic_data import DEMO_CASES, DEMO_PRIORITY_LEADS, DEMO_CROSS_CASE_INSIGHTS

def render_dashboard_view():
    """
    Render main Investigator Dashboard with key operational statistics,
    active case switcher, high-priority suspect alerts, and quick actions.
    """
    active_case_id = st.session_state.get("active_case_id", "FIR-104")
    active_case_meta = next((c for c in DEMO_CASES if c["case_id"] == active_case_id), DEMO_CASES[0])

    # 1. Operational Overview Card
    st.markdown(f"""
    <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 14px; padding: 20px 24px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
        <div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="background: rgba(239, 68, 68, 0.2); color: #ef4444; border: 1px solid #ef4444; padding: 3px 10px; border-radius: 6px; font-weight: 800; font-size: 0.8rem; font-family: 'JetBrains Mono', monospace;">
                    {active_case_meta['status']}
                </span>
                <h2 style="margin: 0; font-size: 1.6rem; color: #ffffff;">{active_case_meta['case_id']} — {active_case_meta['title']}</h2>
            </div>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 0.9rem;">
                📍 <b>Location:</b> {active_case_meta['location']} &nbsp;|&nbsp; 
                📅 <b>Registered:</b> {active_case_meta['date']} &nbsp;|&nbsp; 
                👮 <b>Investigating Officer:</b> {active_case_meta['io_name']} ({active_case_meta['io_badge']})
            </p>
        </div>
        <div>
            <span style="background: rgba(0, 229, 255, 0.1); border: 1px solid rgba(0, 229, 255, 0.35); color: #00e5ff; padding: 8px 16px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; font-family: 'JetBrains Mono', monospace;">
                PRIORITY: {active_case_meta['priority']}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. Main KPI Metrics Row
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Active Cases</div>
            <div class="kpi-value" style="color: #60a5fa;">12</div>
            <div class="kpi-trend">Under Current Unit</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Connected Entities</div>
            <div class="kpi-value" style="color: #00e5ff;">{active_case_meta['entities_count']}</div>
            <div class="kpi-trend">Mapped in Graph</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Cross-Case Links</div>
            <div class="kpi-value" style="color: #f59e0b;">27</div>
            <div class="kpi-trend">Shared Asset Connections</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">High-Priority Alerts</div>
            <div class="kpi-value" style="color: #ef4444;">8</div>
            <div class="kpi-trend">Requires Action</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Urgent Alerts & Recent Cases Row
    col_cases, col_alerts = st.columns([1.5, 1.2])

    with col_cases:
        st.markdown("### 📁 Recent Station Cases")
        st.write("Browse case dossiers or switch active investigation context:")
        
        for c in DEMO_CASES:
            is_active = (c["case_id"] == active_case_id)
            border_col = "rgba(0, 229, 255, 0.6)" if is_active else "rgba(75, 85, 99, 0.3)"
            bg_col = "rgba(0, 229, 255, 0.05)" if is_active else "rgba(15, 23, 42, 0.7)"
            badge_color = "#ef4444" if c["priority"] == "HIGH" else "#f59e0b"

            c_c1, c_c2 = st.columns([3.5, 1.2])
            with c_c1:
                st.markdown(f"""
                <div style="background: {bg_col}; border: 1px solid {border_col}; border-radius: 10px; padding: 14px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <span style="color: #00e5ff; font-weight: 800; font-family: 'JetBrains Mono', monospace; font-size: 0.95rem;">{c['case_id']}</span>
                        <span style="background: {badge_color}22; color: {badge_color}; border: 1px solid {badge_color}; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">{c['priority']}</span>
                    </div>
                    <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{c['title']}</div>
                    <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">📍 {c['location']} &nbsp;|&nbsp; 📅 {c['date']} &nbsp;|&nbsp; IO: {c['io_name']}</div>
                </div>
                """, unsafe_allow_html=True)
            with c_c2:
                if st.button("Open Case", key=f"btn_open_case_{c['case_id']}", use_container_width=True):
                    st.session_state["active_case_id"] = c["case_id"]
                    st.session_state["nav_route"] = "📁 Case Management"
                    st.rerun()

    with col_alerts:
        st.markdown("### 🚨 Investigation Alerts & Insights")
        for ins in DEMO_CROSS_CASE_INSIGHTS:
            sev_color = "#ef4444" if ins["severity"] == "CRITICAL" else "#f59e0b"
            st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.85); border-left: 4px solid {sev_color}; border: 1px solid rgba(75, 85, 99, 0.4); border-left-width: 4px; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: {sev_color}; font-size: 0.75rem; font-weight: 800; font-family: 'JetBrains Mono', monospace;">⚠ {ins['type']}</span>
                    <span style="font-size: 0.75rem; color: #94a3b8;">{ins['confidence']}</span>
                </div>
                <div style="font-size: 0.9rem; font-weight: 700; color: #ffffff; margin: 4px 0;">{ins['title']}</div>
                <div style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.4;">{ins['summary']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr style='border-top: 1px solid rgba(0, 229, 255, 0.2); margin: 25px 0;'>", unsafe_allow_html=True)

    # 4. High-Priority Investigation Leads Preview
    st.markdown("### 🎯 Top Prioritized Investigation Leads")
    st.write("Entities with the highest composite investigation priority scores across current cases:")

    lead_cols = st.columns(3)
    for idx, lead in enumerate(DEMO_PRIORITY_LEADS):
        with lead_cols[idx]:
            score_col = "#ef4444" if lead["score"] >= 80 else "#f59e0b"
            st.markdown(f"""
            <div style="background: rgba(13, 21, 39, 0.9); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 12px; padding: 18px; text-align: center;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-size: 0.75rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;">RANK #{lead['rank']}</span>
                    <span style="color: {score_col}; font-weight: 800; font-size: 0.8rem;">{lead['level']}</span>
                </div>
                <h3 style="margin: 8px 0 2px 0; color: #ffffff; font-size: 1.25rem;">{lead['name']}</h3>
                <div style="color: #94a3b8; font-size: 0.8rem; margin-bottom: 12px;">Type: {lead['type']}</div>
                <div style="font-size: 2.2rem; font-weight: 800; color: {score_col}; margin: 8px 0; font-family: 'Outfit', sans-serif;">
                    {lead['score']}<span style="font-size: 1rem; color: #94a3b8;">/100</span>
                </div>
                <div style="font-size: 0.75rem; color: #cbd5e1; text-align: left; background: rgba(0,0,0,0.3); padding: 8px; border-radius: 6px;">
                    • {lead['reasons'][0]}<br>
                    • {lead['reasons'][1]}
                </div>
            </div>
            """, unsafe_allow_html=True)
