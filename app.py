"""
CrimeLens — AI-Assisted Crime Intelligence & Investigation Support Platform
Main Application Entry Point (Connect ➔ Analyze ➔ Visualize ➔ Investigate)
"""
import streamlit as st
from src.core.config import PAGE_TITLE, PAGE_ICON, DEMO_CREDENTIALS
from src.utils.styles import apply_custom_styles
from src.components.header import render_header
from src.components.sidebar import render_sidebar
from src.components.floating_assistant import render_floating_assistant

# Public Views
from src.views.landing import render_landing_view
from src.views.auth import render_login_view, render_register_view

# Investigation Suite Views
from src.views.dashboard import render_dashboard_view
from src.views.cases import render_cases_view
from src.views.data_hub import render_data_hub_view
from src.views.entity_resolution import render_entity_resolution_view
from src.views.knowledge_graph import render_knowledge_graph_view
from src.views.insights import render_insights_view
from src.views.priority import render_priority_view
from src.views.chatbot import render_chatbot_view
from src.views.reports import render_reports_view

# 1. Streamlit Configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Cyberpunk / Intelligence Dark Theme CSS
apply_custom_styles()

# 3. Handle Query Params Navigation (e.g. from floating assistant)
if hasattr(st, "query_params") and "page" in st.query_params:
    qp = str(st.query_params.get("page", "")).lower()
    if qp in ["chatbot", "ask", "assistant"]:
        if "authenticated_user" not in st.session_state or not st.session_state["authenticated_user"]:
            st.session_state["authenticated_user"] = DEMO_CREDENTIALS
        st.session_state["nav_route"] = "💬 Ask CrimeLens (AI Assistant)"
        try:
            st.query_params.clear()
        except Exception:
            pass

# 4. Render Sidebar Navigation & Collect State
auth_state, selected_route = render_sidebar()

# 5. Route to Active Screen
if auth_state == "public":
    if selected_route == "🌐 Landing Page":
        render_landing_view()
    elif selected_route == "🔐 Investigator Login":
        render_login_view()
    elif selected_route == "📝 Register Investigator":
        render_register_view()

else:
    # Authenticated Command Suite
    render_header()

    if selected_route == "📊 Investigator Dashboard":
        render_dashboard_view()

    elif selected_route == "📁 Case Management":
        render_cases_view()

    elif selected_route == "📥 Data Intelligence Hub":
        render_data_hub_view()

    elif selected_route == "🧬 Entity Extraction & Resolution":
        render_entity_resolution_view()

    elif selected_route == "🕸️ Knowledge Graph Workspace":
        render_knowledge_graph_view()

    elif selected_route == "⚠️ Investigation Insights & Timeline":
        render_insights_view()

    elif selected_route == "🎯 Investigation Priority Leads":
        render_priority_view()

    elif selected_route == "💬 Ask CrimeLens (AI Assistant)":
        render_chatbot_view()

    elif selected_route == "📄 Investigation Report Generator":
        render_reports_view()

    # Floating 3D Assistant Widget (Docked in viewport)
    render_floating_assistant(selected_route)

# 6. Global Page Footer
st.markdown("<br><hr style='border-top: 1px solid rgba(0, 229, 255, 0.15); margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 12px 0 10px 0; color: #94a3b8; font-size: 0.85rem;">
    <span>CrimeLens Investigation Platform • Developed for Smart India Hackathon • Built with ❤️ by </span>
    <a href="https://github.com/AviBhosale01" target="_blank" style="color: #00e5ff; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 5px;">
        Avii
        <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor" style="vertical-align: middle; fill: #00e5ff;"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
    </a>
</div>
""", unsafe_allow_html=True)
