"""
CrimeLens - Explainable Investigation Priority Module
Ranks suspect leads using transparent, defensible scoring factors (USP 6).
"""
import streamlit as st
from src.core.synthetic_data import DEMO_PRIORITY_LEADS
from src.utils.styles import render_html

def render_priority_view():
    """
    Render Explainable Investigation Priority page showing ranked leads,
    factor breakdowns, underlying evidence tags, and statutory legal disclaimers.
    """
    st.markdown("## 🎯 Explainable Investigation Priority (USP 06)")
    st.write("Prioritizes persons of interest, suspect vehicles, and communication nodes based on transparent multi-factor network connectivity rather than opaque black-box scoring.")

    # Statutory Disclaimer Banner
    render_html("""
    <div style="background: rgba(245, 158, 11, 0.1); border-left: 4px solid #f59e0b; border: 1px solid rgba(245, 158, 11, 0.35); border-left-width: 4px; border-radius: 8px; padding: 14px 18px; margin-bottom: 25px;">
        <div style="font-weight: 800; color: #fbbf24; font-size: 0.95rem; margin-bottom: 4px;">
            ⚖️ STATUTORY INVESTIGATION DISCLAIMER
        </div>
        <div style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.5;">
            The <b>Investigation Priority Score</b> is an algorithmic dispatch heuristic designed solely to assist supervisory officers in triaging investigative leads and evidence verification. 
            <b>This score does NOT constitute proof of guilt, criminality, or probable cause.</b> Final determination rests solely with judicial and sworn police authorities.
        </div>
    </div>
    """)

    # Lead Cards
    for lead in DEMO_PRIORITY_LEADS:
        score = lead["score"]
        score_color = "#ef4444" if score >= 80 else "#f59e0b"
        bd = lead["breakdown"]

        with st.container():
            render_html(f"""
            <div style="background: rgba(13, 21, 39, 0.9); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 14px; padding: 22px; margin-bottom: 22px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;">
                            RANK #{lead['rank']}
                        </span>
                        <h3 style="margin: 0; color: #ffffff; font-size: 1.35rem;">{lead['name']}</h3>
                        <span style="color: #94a3b8; font-size: 0.85rem;">(Type: {lead['type']})</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="background: {score_color}22; color: {score_color}; border: 1px solid {score_color}; padding: 4px 12px; border-radius: 20px; font-weight: 800; font-size: 0.8rem;">
                            {lead['level']}
                        </span>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 20px; align-items: center;">
                    <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 10px; padding: 18px; text-align: center;">
                        <div style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;">
                            Composite Priority Index
                        </div>
                        <div style="font-size: 3.2rem; font-weight: 900; color: {score_color}; font-family: 'Outfit', sans-serif; line-height: 1.1; margin: 6px 0;">
                            {score}<span style="font-size: 1.3rem; color: #64748b;">/100</span>
                        </div>
                        <div style="font-size: 0.75rem; color: #34d399; font-weight: 600;">
                            ✓ Verified Across 4 Evidence Sources
                        </div>
                    </div>

                    <div>
                        <b style="color: #00e5ff; font-size: 0.9rem;">Explainable Factor Breakdown:</b>
                        <div style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                <span>1. Network &amp; Associate Connectivity</span>
                                <b style="color: #ffffff; font-family: 'JetBrains Mono', monospace;">{bd['network_connectivity']['score']} / {bd['network_connectivity']['max']}</b>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                <span>2. Cross-Case Link Multiplier</span>
                                <b style="color: #ffffff; font-family: 'JetBrains Mono', monospace;">{bd['cross_case_links']['score']} / {bd['cross_case_links']['max']}</b>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                <span>3. Anomalous Financial Transaction Flow</span>
                                <b style="color: #ffffff; font-family: 'JetBrains Mono', monospace;">{bd['transaction_pattern']['score']} / {bd['transaction_pattern']['max']}</b>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                <span>4. Primary Physical &amp; Telecommunication Evidence</span>
                                <b style="color: #ffffff; font-family: 'JetBrains Mono', monospace;">{bd['evidence_strength']['score']} / {bd['evidence_strength']['max']}</b>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(75, 85, 99, 0.35); border-radius: 8px; padding: 12px 16px; margin-top: 16px;">
                    <b style="color: #ffffff; font-size: 0.85rem;">Why this lead was prioritized:</b>
                    <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6; margin-top: 6px;">
                        {"<br>".join(f"✓ {r}" for r in lead['reasons'])}
                    </div>
                    <div style="margin-top: 10px; font-size: 0.78rem; color: #94a3b8;">
                        Evidence Sources: <span style="color: #00e5ff; font-family: 'JetBrains Mono', monospace; font-weight: 700;">{" ".join(f'[{e}]' for e in lead['evidence'])}</span>
                    </div>
                </div>
            </div>
            """)
