"""
CrimeLens - Application Header Component
"""
import streamlit as st
from src.utils.styles import render_html

def render_header():
    """
    Render the top dashboard banner with CrimeLens intelligence branding,
    active case indicator, and investigator clearance pill using clean columns.
    """
    user = st.session_state.get("authenticated_user", None)
    active_case_id = st.session_state.get("active_case_id", "FIR-104")

    col_brand, col_pill = st.columns([2.6, 1.4])

    with col_brand:
        render_html("""
        <div style="display: flex; align-items: center; gap: 14px;">
            <div style="background: linear-gradient(135deg, #00e5ff, #2563eb); width: 46px; height: 46px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 4px 15px rgba(0, 229, 255, 0.4); flex-shrink: 0;">
                🔍
            </div>
            <div>
                <h1 style="margin: 0; font-size: 2rem; background: linear-gradient(to right, #ffffff, #00e5ff, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1; white-space: nowrap;">CrimeLens</h1>
                <p style="margin: 2px 0 0 0; color: #94a3b8; font-size: 0.88rem; font-weight: 500; white-space: nowrap;">
                    AI-Assisted Crime Intelligence &amp; Investigation Support Platform
                </p>
            </div>
        </div>
        """)

    with col_pill:
        if user:
            user_name = user.get("name", "Investigator")
            user_badge = user.get("badge_id", "ACTIVE")
            render_html(f"""
            <div style="text-align: right; padding-top: 6px;">
                <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(0, 229, 255, 0.1); border: 1px solid rgba(0, 229, 255, 0.35); padding: 6px 14px; border-radius: 20px;">
                    <span style="width: 8px; height: 8px; border-radius: 50%; background: #00e5ff; box-shadow: 0 0 8px #00e5ff; display: inline-block;"></span>
                    <span style="color: #00e5ff; font-size: 0.85rem; font-weight: 700; font-family: 'JetBrains Mono', monospace;">CASE: {active_case_id}</span>
                    <span style="color: #64748b;">|</span>
                    <span style="color: #e2e8f0; font-size: 0.85rem; font-weight: 600;">{user_name} ({user_badge})</span>
                </div>
            </div>
            """)
        else:
            render_html("""
            <div style="text-align: right; padding-top: 8px;">
                <span style="background-color: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); color: #93c5fd; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; font-family: 'JetBrains Mono', monospace;">
                    PUBLIC PORTAL / LAW ENFORCEMENT
                </span>
            </div>
            """)

    render_html("<hr style='border-top: 1px solid rgba(0, 229, 255, 0.18); margin: 10px 0 20px 0;'>")
