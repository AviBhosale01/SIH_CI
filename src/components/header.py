"""
CrimeLens - Application Header Component
"""
import streamlit as st

def render_header():
    """
    Render the top dashboard banner with CrimeLens intelligence branding,
    active case indicator, and investigator clearance pill.
    """
    user = st.session_state.get("authenticated_user", None)
    active_case_id = st.session_state.get("active_case_id", "FIR-104")
    
    auth_pill = ""
    if user:
        user_name = user.get("name", "Investigator")
        user_badge = user.get("badge_id", "ACTIVE")
        auth_pill = f"""
        <div style="text-align: right;">
            <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(0, 229, 255, 0.1); border: 1px solid rgba(0, 229, 255, 0.35); padding: 5px 12px; border-radius: 20px;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #00e5ff; box-shadow: 0 0 8px #00e5ff;"></span>
                <span style="color: #00e5ff; font-size: 0.85rem; font-weight: 700; font-family: 'JetBrains Mono', monospace;">CASE: {active_case_id}</span>
                <span style="color: #64748b;">|</span>
                <span style="color: #e2e8f0; font-size: 0.85rem; font-weight: 600;">{user_name} ({user_badge})</span>
            </div>
        </div>
        """
    else:
        auth_pill = """
        <div style="text-align: right;">
            <span style="background-color: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); color: #93c5fd; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; font-family: 'JetBrains Mono', monospace;">
                PUBLIC PORTAL / CLEARED FOR LAW ENFORCEMENT
            </span>
        </div>
        """

    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; border-bottom: 1px solid rgba(0, 229, 255, 0.18); padding-bottom: 14px;">
        <div style="display: flex; align-items: center; gap: 14px;">
            <div style="background: linear-gradient(135deg, #00e5ff, #2563eb); width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 4px 15px rgba(0, 229, 255, 0.4);">
                🔍
            </div>
            <div>
                <h1 style="margin: 0; font-size: 1.9rem; background: linear-gradient(to right, #ffffff, #00e5ff, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1;">CrimeLens</h1>
                <p style="margin: 3px 0 0 0; color: #94a3b8; font-size: 0.88rem; font-weight: 500;">
                    AI-Assisted Crime Intelligence &amp; Investigation Support Platform
                </p>
            </div>
        </div>
        {auth_pill}
    </div>
    """, unsafe_allow_html=True)
