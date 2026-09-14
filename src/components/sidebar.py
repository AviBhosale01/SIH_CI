"""
CrimeLens - Sidebar Navigation & Workspace Controls
"""
import streamlit as st
from src.core.config import DEMO_CREDENTIALS
from src.core.synthetic_data import DEMO_CASES

def render_sidebar():
    """
    Render CrimeLens navigation sidebar with investigator profile,
    active case selector, module routes, and quick demo switcher.
    """
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 10px 0 15px 0;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 10px; background: linear-gradient(135deg, #00e5ff, #1d4ed8); font-size: 1.3rem; margin-bottom: 8px; box-shadow: 0 0 16px rgba(0, 229, 255, 0.4);">
            🔍
        </div>
        <h3 style="margin: 0; color: #ffffff; font-family: 'Outfit', sans-serif; font-size: 1.35rem; letter-spacing: -0.01em;">CrimeLens</h3>
        <p style="margin: 2px 0 0 0; color: #00e5ff; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;">Investigation Suite</p>
    </div>
    <hr style="border-top: 1px solid rgba(0, 229, 255, 0.15); margin: 0 0 15px 0;">
    """, unsafe_allow_html=True)

    user = st.session_state.get("authenticated_user", None)

    # 1. AUTHENTICATED INVESTIGATOR WORKSPACE
    if user:
        # Investigator Profile Card
        st.sidebar.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 10px; padding: 12px; margin-bottom: 15px;">
            <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Active Investigator</div>
            <div style="font-size: 0.95rem; color: #ffffff; font-weight: 700;">{user.get('name', 'Investigator')}</div>
            <div style="font-size: 0.78rem; color: #00e5ff; font-family: 'JetBrains Mono', monospace;">Badge: {user.get('badge_id', 'MH-PN-4082')}</div>
            <div style="font-size: 0.75rem; color: #cbd5e1; margin-top: 4px;">{user.get('department', 'Crime Branch')}</div>
        </div>
        """, unsafe_allow_html=True)

        # Active Case Selector
        st.sidebar.markdown("##### 📁 Active Case Context")
        case_options = {c["case_id"]: f"{c['case_id']} — {c['title'][:22]}..." for c in DEMO_CASES}
        current_case = st.session_state.get("active_case_id", "FIR-104")
        case_keys = list(case_options.keys())
        default_case_idx = case_keys.index(current_case) if current_case in case_keys else 0

        selected_case_id = st.sidebar.selectbox(
            "Select Working Case",
            case_keys,
            index=default_case_idx,
            format_func=lambda x: case_options[x],
            key="sb_active_case_sel"
        )
        st.session_state["active_case_id"] = selected_case_id

        st.sidebar.markdown("<hr style='border-top: 1px solid rgba(75, 85, 99, 0.25); margin: 12px 0;'>", unsafe_allow_html=True)

        # Main Investigation Routes
        nav_options = [
            "📊 Investigator Dashboard",
            "📁 Case Management",
            "📥 Data Intelligence Hub",
            "🧬 Entity Extraction & Resolution",
            "🕸️ Knowledge Graph Workspace",
            "⚠️ Investigation Insights & Timeline",
            "🎯 Investigation Priority Leads",
            "💬 Ask CrimeLens (AI Assistant)",
            "📄 Investigation Report Generator"
        ]

        # Handle programmatic navigation requests
        if "requested_page" in st.session_state and st.session_state["requested_page"]:
            req_p = st.session_state.pop("requested_page")
            if req_p in nav_options:
                st.session_state["nav_route"] = req_p

        if "nav_route" not in st.session_state or st.session_state["nav_route"] not in nav_options:
            st.session_state["nav_route"] = "📊 Investigator Dashboard"

        selected_nav = st.sidebar.radio("Investigation Modules", nav_options, key="nav_route")

        # Workspace actions
        st.sidebar.markdown("<hr style='border-top: 1px solid rgba(75, 85, 99, 0.25); margin: 15px 0;'>", unsafe_allow_html=True)
        col_act1, col_act2 = st.sidebar.columns(2)
        with col_act1:
            if st.button("🌐 Landing", key="btn_sb_landing", use_container_width=True):
                st.session_state["public_page"] = "landing"
                st.session_state["authenticated_user"] = None
                st.rerun()
        with col_act2:
            if st.button("🚪 Logout", key="btn_sb_logout", use_container_width=True):
                st.session_state["authenticated_user"] = None
                st.session_state["public_page"] = "login"
                st.rerun()

        return "authenticated", selected_nav

    # 2. PUBLIC / PRE-LOGIN NAVIGATION
    else:
        st.sidebar.markdown("##### 🔐 Investigation Portal Access")
        public_routes = [
            "🌐 Landing Page",
            "🔐 Investigator Login",
            "📝 Register Investigator"
        ]

        if "public_page" not in st.session_state:
            st.session_state["public_page"] = "🌐 Landing Page"

        cur_public = st.session_state.get("public_page", "🌐 Landing Page")
        if cur_public not in public_routes:
            cur_public = "🌐 Landing Page"
        
        default_p_idx = public_routes.index(cur_public) if cur_public in public_routes else 0
        selected_public = st.sidebar.radio("Portal Navigation", public_routes, index=default_p_idx, key="public_nav_radio")
        st.session_state["public_page"] = selected_public

        st.sidebar.markdown("<hr style='border-top: 1px solid rgba(0, 229, 255, 0.15); margin: 15px 0;'>", unsafe_allow_html=True)
        st.sidebar.markdown("""
        <div style="background: rgba(0, 229, 255, 0.06); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 8px; padding: 10px; text-align: center; margin-bottom: 12px;">
            <div style="font-size: 0.75rem; color: #00e5ff; font-weight: 700; text-transform: uppercase;">🚀 Hackathon Evaluator Access</div>
            <div style="font-size: 0.78rem; color: #e2e8f0; margin-top: 3px;">Launch instant authenticated demo session for PI Vikram Patil.</div>
        </div>
        """, unsafe_allow_html=True)

        if st.sidebar.button("⚡ 1-Click Demo Login (FIR-104)", key="btn_1click_demo_sb", use_container_width=True):
            st.session_state["authenticated_user"] = DEMO_CREDENTIALS
            st.session_state["active_case_id"] = "FIR-104"
            st.session_state["nav_route"] = "📊 Investigator Dashboard"
            st.rerun()

        return "public", selected_public
