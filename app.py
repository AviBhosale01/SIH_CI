"""
CrimeLens — AI-Assisted Crime Intelligence & Investigation Support Platform
Main Application Entry Point (Connect ➔ Analyze ➔ Visualize ➔ Investigate)
"""
import streamlit as st
from src.core.config import PAGE_TITLE, PAGE_ICON, DEMO_CREDENTIALS
from src.utils.styles import apply_custom_styles, render_html
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
render_html("<br><hr style='border-top: 1px solid rgba(0, 229, 255, 0.15); margin-top: 40px;'>")
render_html("""
<div style="text-align: center; padding: 12px 0 10px 0; color: #94a3b8; font-size: 0.85rem;">
    <span>CrimeLens Investigation Platform • Developed for Smart India Hackathon</span>
</div>
""")

