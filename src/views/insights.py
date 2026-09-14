"""
CrimeLens - Investigation Insights & Temporal Analysis Module
Surfaces automated cross-case link discovery, unusual communication patterns,
financial correlations, and 72-hour incident timelines.
"""
import streamlit as st
from src.core.synthetic_data import DEMO_CROSS_CASE_INSIGHTS, DEMO_TIMELINE
from src.utils.styles import render_html

def render_insights_view():
    """
    Render CrimeLens Investigation Insights showcasing cross-case discoveries (USP 4),
    anomalous patterns, and chronological timeline analysis.
    """
    st.markdown("## ⚠️ Investigation Insights & Cross-Case Discovery")
    st.write("Synthesizes multi-source correlations to uncover hidden cross-case links and temporal crime event sequences.")

    tab_insights, tab_timeline = st.tabs(["🚨 Cross-Case Discoveries & Patterns", "📅 72-Hour Temporal Incident Timeline"])

    with tab_insights:
        st.markdown("### 🚨 High-Confidence Cross-Case Correlations (USP 04)")
        st.write("Identifies shared physical assets, co-offender networks, and financial conduits linking separate police cases:")

        for ins in DEMO_CROSS_CASE_INSIGHTS:
            is_critical = (ins["severity"] == "CRITICAL")
            border_col = "rgba(239, 68, 68, 0.7)" if is_critical else "rgba(245, 158, 11, 0.7)"
            bg_col = "rgba(239, 68, 68, 0.08)" if is_critical else "rgba(245, 158, 11, 0.08)"
            badge_col = "#ef4444" if is_critical else "#f59e0b"

            with st.container():
                render_html(f"""
                <div style="background: {bg_col}; border: 1px solid {border_col}; border-radius: 12px; padding: 20px; margin-bottom: 18px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="background: {badge_col}22; color: {badge_col}; border: 1px solid {badge_col}; font-size: 0.75rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;">
                                {ins['severity']}
                            </span>
                            <span style="color: #00e5ff; font-weight: 800; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;">{ins['insight_id']}</span>
                            <span style="color: #ffffff; font-weight: 700; font-size: 1.1rem;">{ins['title']}</span>
                        </div>
                        <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-size: 0.75rem; font-weight: 700; padding: 2px 10px; border-radius: 20px;">
                            Confidence: {ins['confidence']}
                        </span>
                    </div>

                    <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.5; margin: 10px 0 14px 0;">{ins['summary']}</p>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; background: rgba(0,0,0,0.3); padding: 12px; border-radius: 8px; font-size: 0.82rem;">
                        <div>
                            <span style="color: #94a3b8;">Linked Cases:</span><br>
                            <b style="color: #ef4444; font-family: 'JetBrains Mono', monospace;">{" ⟷ ".join(ins['cases_involved'])}</b>
                        </div>
                        <div>
                            <span style="color: #94a3b8;">Entities Involved:</span><br>
                            <b style="color: #ffffff;">{", ".join(ins['entities_involved'])}</b>
                        </div>
                        <div>
                            <span style="color: #94a3b8;">Underlying Evidence Tags:</span><br>
                            <span style="color: #00e5ff; font-family: 'JetBrains Mono', monospace; font-weight: 700;">{" ".join(f'[{e}]' for e in ins['evidence_sources'])}</span>
                        </div>
                    </div>
                </div>
                """)

    with tab_timeline:
        st.markdown("### 📅 72-Hour Temporal Incident Timeline")
        st.write("Chronological sequence of physical movements, telecommunications, and financial transactions leading up to and immediately following the incident:")

        render_html("""
        <div style="background: rgba(0, 229, 255, 0.08); border: 1px solid rgba(0, 229, 255, 0.3); border-radius: 8px; padding: 12px 16px; margin-bottom: 20px;">
            <b style="color: #00e5ff;">⚡ Temporal Cluster Insight:</b>
            <span style="color: #cbd5e1; font-size: 0.88rem;">
                Four interconnected investigative events occurred within a concentrated <b>72-hour window</b> (Aug 10 to Aug 13, 2026), indicating deliberate coordination between prime suspect and transport associate.
            </span>
        </div>
        """)

        for step_idx, step in enumerate(DEMO_TIMELINE):
            b_color = "#f59e0b" if step["type"] == "vehicle" else ("#10b981" if step["type"] == "cdr" else ("#ef4444" if step["type"] == "fir" else "#06b6d4"))

            render_html(f"""
            <div style="display: flex; gap: 16px; margin-bottom: 18px; position: relative;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div style="width: 32px; height: 32px; border-radius: 50%; background: {b_color}; color: #0a0f1d; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.85rem; box-shadow: 0 0 12px {b_color};">
                        {step_idx + 1}
                    </div>
                    {"<div style='width: 2px; height: 65px; background: rgba(75, 85, 99, 0.4); margin-top: 4px;'></div>" if step_idx < len(DEMO_TIMELINE)-1 else ""}
                </div>
                <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 10px; padding: 14px 18px; flex: 1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <span style="color: #00e5ff; font-weight: 800; font-size: 0.82rem; font-family: 'JetBrains Mono', monospace;">📅 {step['date']} • {step['time']}</span>
                        <span style="background: {b_color}22; color: {b_color}; border: 1px solid {b_color}; font-size: 0.72rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;">{step['badge']}</span>
                    </div>
                    <h4 style="margin: 4px 0; color: #ffffff; font-size: 1.05rem;">{step['title']}</h4>
                    <p style="color: #cbd5e1; font-size: 0.85rem; margin: 0 0 8px 0; line-height: 1.4;">{step['description']}</p>
                    <div style="font-size: 0.75rem; color: #94a3b8;">
                        Case Link: <b style="color: #ef4444; font-family: 'JetBrains Mono', monospace;">{step['case_id']}</b> &nbsp;|&nbsp; 
                        Evidence Record: <span style="color: #00e5ff; font-family: 'JetBrains Mono', monospace;">[{step['evidence']}]</span>
                    </div>
                </div>
            </div>
            """)
