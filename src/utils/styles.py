"""
UI Styles & Custom CSS Module for CrimeLens
"""
import streamlit as st

def apply_custom_styles():
    """
    Inject modern cybersecurity / police intelligence dark theme CSS,
    neon cyan accents, subtle glowing nodes, and clean responsive layouts.
    """
    st.markdown("""
    <head>
        <meta name="description" content="CrimeLens: AI-Assisted Crime Intelligence & Investigation Support Platform">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    </head>
    <style>
        /* Base dark intelligence canvas */
        .stApp {
            background-color: #0a0f1d;
            background-image: 
                radial-gradient(rgba(0, 229, 255, 0.05) 1px, transparent 0),
                radial-gradient(rgba(59, 130, 246, 0.04) 1px, transparent 0);
            background-size: 32px 32px;
            background-position: 0 0, 16px 16px;
            color: #f1f5f9;
            font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #0d1527 !important;
            border-right: 1px solid rgba(0, 229, 255, 0.15) !important;
        }

        /* Header typography */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }

        /* Accessibility text contrast */
        p, span, label, caption, .stCaption {
            color: #cbd5e1 !important;
        }

        /* Monospace badges & IDs */
        code, .mono-badge {
            font-family: 'JetBrains Mono', monospace !important;
        }

        /* CrimeLens Hero & Cards */
        .crimelens-hero {
            background: linear-gradient(135deg, rgba(13, 21, 39, 0.95), rgba(15, 23, 42, 0.85));
            border: 1px solid rgba(0, 229, 255, 0.25);
            border-radius: 16px;
            padding: 36px 30px;
            margin-bottom: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), inset 0 0 20px rgba(0, 229, 255, 0.05);
            position: relative;
            overflow: hidden;
        }

        .crimelens-hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 229, 255, 0.08) 0%, transparent 60%);
            pointer-events: none;
        }

        .kpi-card {
            background: rgba(13, 21, 39, 0.90);
            border: 1px solid rgba(0, 229, 255, 0.20);
            border-radius: 14px;
            padding: 18px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .kpi-card:hover {
            transform: translateY(-3px);
            border-color: rgba(0, 229, 255, 0.5);
            box-shadow: 0 10px 25px rgba(0, 229, 255, 0.15);
        }

        .kpi-title {
            font-size: 0.8rem;
            color: #94a3b8 !important;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin-bottom: 6px;
        }

        .kpi-value {
            font-size: 2rem;
            font-weight: 800;
            color: #ffffff !important;
            font-family: 'Outfit', sans-serif;
        }

        .kpi-trend {
            font-size: 0.75rem;
            margin-top: 4px;
            font-weight: 600;
            color: #00e5ff !important;
        }

        /* USP demonstration card */
        .usp-card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(59, 130, 246, 0.25);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            height: 100%;
            transition: all 0.2s ease;
        }

        .usp-card:hover {
            border-color: #00e5ff;
            background: rgba(15, 23, 42, 0.95);
            box-shadow: 0 8px 24px rgba(0, 229, 255, 0.12);
        }

        /* Crime alert banners */
        .alert-banner {
            padding: 14px 18px;
            border-radius: 10px;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .alert-critical {
            background: rgba(239, 68, 68, 0.12);
            border-left: 4px solid #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.3);
            border-left-width: 4px;
        }

        .alert-warning {
            background: rgba(245, 158, 11, 0.12);
            border-left: 4px solid #f59e0b;
            border: 1px solid rgba(245, 158, 11, 0.3);
            border-left-width: 4px;
        }

        .alert-info {
            background: rgba(0, 229, 255, 0.10);
            border-left: 4px solid #00e5ff;
            border: 1px solid rgba(0, 229, 255, 0.25);
            border-left-width: 4px;
        }

        /* Custom buttons styling */
        .stButton > button {
            border-radius: 8px !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em !important;
            transition: all 0.2s ease !important;
        }

        .stButton > button:hover {
            border-color: #00e5ff !important;
            box-shadow: 0 0 12px rgba(0, 229, 255, 0.35) !important;
        }

        /* Timeline step node */
        .timeline-step {
            display: flex;
            gap: 16px;
            margin-bottom: 20px;
            position: relative;
        }

        .timeline-bullet {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #00e5ff;
            color: #0a0f1d;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 0.8rem;
            flex-shrink: 0;
            box-shadow: 0 0 10px rgba(0, 229, 255, 0.6);
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 1px solid rgba(0, 229, 255, 0.2);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 6px 6px 0 0;
            color: #94a3b8 !important;
            font-weight: 600;
            padding: 8px 16px;
        }

        .stTabs [aria-selected="true"] {
            background-color: rgba(0, 229, 255, 0.12) !important;
            color: #00e5ff !important;
            border-bottom: 2px solid #00e5ff !important;
        }
    </style>
    """, unsafe_allow_html=True)
