"""
CrimeLens - Landing Page View Module
Demonstrates the 6 core USPs of CrimeLens with a high-impact cybersecurity/intelligence aesthetic.
"""
import streamlit as st
from src.core.config import DEMO_CREDENTIALS

def render_landing_view():
    """
    Render the public landing page showcasing the 6 key USPs of CrimeLens,
    live architecture, and direct navigation to authentication/demo.
    """
    # 1. Hero Section
    st.markdown("""
    <div class="crimelens-hero">
        <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(0, 229, 255, 0.12); border: 1px solid rgba(0, 229, 255, 0.4); padding: 5px 14px; border-radius: 20px; margin-bottom: 16px;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #00e5ff; box-shadow: 0 0 10px #00e5ff;"></span>
            <span style="color: #00e5ff; font-size: 0.8rem; font-weight: 800; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.08em; text-transform: uppercase;">
                Operational Intelligence Platform v3.0
            </span>
        </div>
        <h1 style="font-size: 3.2rem; font-weight: 800; margin: 0 0 12px 0; line-height: 1.1; background: linear-gradient(135deg, #ffffff 40%, #00e5ff 85%, #3b82f6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            CrimeLens
        </h1>
        <h3 style="font-size: 1.5rem; color: #00e5ff; font-weight: 600; margin: 0 0 16px 0; font-family: 'Outfit', sans-serif;">
            Connect Evidence. Reveal Relationships. Accelerate Investigations.
        </h3>
        <p style="font-size: 1.1rem; color: #cbd5e1; max-width: 850px; line-height: 1.6; margin-bottom: 24px;">
            CrimeLens transforms fragmented crime records into a connected, explainable investigation workspace. Unify disparate FIRs, CDR telecommunications, financial trails, ANPR vehicle tracking, and informant intelligence into a single operational canvas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Hero Action Call-to-Actions
    btn_col1, btn_col2, btn_col3, _ = st.columns([1.3, 1.3, 1.8, 1.5])
    with btn_col1:
        if st.button("🔐 Investigator Login", key="btn_hero_login", use_container_width=True):
            st.session_state["public_page"] = "🔐 Investigator Login"
            st.rerun()
    with btn_col2:
        if st.button("📝 Register Investigator", key="btn_hero_register", use_container_width=True):
            st.session_state["public_page"] = "📝 Register Investigator"
            st.rerun()
    with btn_col3:
        if st.button("⚡ 1-Click Hero Demo (FIR-104)", key="btn_hero_demo", use_container_width=True):
            st.session_state["authenticated_user"] = DEMO_CREDENTIALS
            st.session_state["active_case_id"] = "FIR-104"
            st.session_state["nav_route"] = "📊 Investigator Dashboard"
            st.rerun()

    st.markdown("<br><hr style='border-top: 1px solid rgba(0, 229, 255, 0.2); margin: 30px 0;'>", unsafe_allow_html=True)

    # 2. Core Philosophy Bar: Connect -> Analyze -> Visualize -> Investigate
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(13, 21, 39, 0.7); border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 12px; padding: 18px 24px; margin-bottom: 35px; text-align: center;">
        <div style="flex: 1;">
            <div style="font-size: 1.2rem;">🔗</div>
            <div style="font-weight: 700; color: #00e5ff; font-size: 0.95rem;">1. CONNECT</div>
            <div style="font-size: 0.75rem; color: #94a3b8;">FIR + CDR + Bank + Vehicle</div>
        </div>
        <div style="color: #3b82f6; font-size: 1.2rem;">➔</div>
        <div style="flex: 1;">
            <div style="font-size: 1.2rem;">🧬</div>
            <div style="font-weight: 700; color: #00e5ff; font-size: 0.95rem;">2. RESOLVE</div>
            <div style="font-size: 0.75rem; color: #94a3b8;">Entity Deduplication (97%)</div>
        </div>
        <div style="color: #3b82f6; font-size: 1.2rem;">➔</div>
        <div style="flex: 1;">
            <div style="font-size: 1.2rem;">🕸️</div>
            <div style="font-weight: 700; color: #00e5ff; font-size: 0.95rem;">3. VISUALIZE</div>
            <div style="font-size: 0.75rem; color: #94a3b8;">Dynamic Knowledge Graph</div>
        </div>
        <div style="color: #3b82f6; font-size: 1.2rem;">➔</div>
        <div style="flex: 1;">
            <div style="font-size: 1.2rem;">🎯</div>
            <div style="font-weight: 700; color: #00e5ff; font-size: 0.95rem;">4. INVESTIGATE</div>
            <div style="font-size: 0.75rem; color: #94a3b8;">Priority Leads & Evidence</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. Six Demonstrable USPs Section
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h2 style="font-size: 1.8rem; margin: 0 0 6px 0;">🛡️ Core Architectural USPs</h2>
        <p style="color: #94a3b8; margin: 0;">Transparent, verifiable capabilities built for modern law-enforcement investigation agencies.</p>
    </div>
    """, unsafe_allow_html=True)

    usp_col1, usp_col2 = st.columns(2)

    with usp_col1:
        # USP 1
        st.markdown("""
        <div class="usp-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">USP 01</span>
                <h4 style="margin: 0; color: #ffffff;">Unified Investigation View</h4>
            </div>
            <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;">
                <b>The Problem</b>: Crucial evidence is fragmented across separate police stations, CDR spreadsheets, bank extracts, and toll records.<br>
                <b>CrimeLens Solution</b>: Automatically models disparate evidentiary streams into a single relational investigation path.
            </p>
            <div style="background: rgba(0,0,0,0.3); border: 1px dashed rgba(0, 229, 255, 0.3); border-radius: 8px; padding: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #00e5ff; text-align: center;">
                FIR-104 ➔ Person (Rahul) ➔ Phone (+91 98765...) ➔ Vehicle (MH12AB1234) ➔ TXN-203 ➔ Related Case (FIR-087)
            </div>
        </div>
        """, unsafe_allow_html=True)

        # USP 3
        st.markdown("""
        <div class="usp-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">USP 03</span>
                <h4 style="margin: 0; color: #ffffff;">Relationship-Based Knowledge Graph</h4>
            </div>
            <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;">
                Instead of static tables, CrimeLens models investigations as multi-dimensional graphs showing how associates, call volumes, shared assets, and locations intersect.
            </p>
            <div style="background: rgba(0,0,0,0.3); border: 1px dashed rgba(59, 130, 246, 0.3); border-radius: 8px; padding: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #93c5fd;">
                Amit Verma &lt;──[14 CDR Calls]──&gt; Rahul Sharma &lt;──[Uses]──&gt; MH12AB1234 &lt;──[Spotted At]──&gt; Swargate (Case FIR-087)
            </div>
        </div>
        """, unsafe_allow_html=True)

        # USP 5
        st.markdown("""
        <div class="usp-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">USP 05</span>
                <h4 style="margin: 0; color: #ffffff;">100% Evidence Traceability</h4>
            </div>
            <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;">
                Every analytical output, relationship edge, and prioritized suspect provides instant citation tags linking back to official underlying police records.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span style="background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace;">[FIR-104] Kothrud</span>
                <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace;">[CDR-202] Vi/Airtel</span>
                <span style="background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace;">[VEH-019] RTO/ANPR</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with usp_col2:
        # USP 2
        st.markdown("""
        <div class="usp-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">USP 02</span>
                <h4 style="margin: 0; color: #ffffff;">Entity Resolution &amp; Deduplication</h4>
            </div>
            <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;">
                Identifies duplicate suspects across misspelled station logs (*Rahul Sharma* in FIR-104 vs *Rahul Sharm* in CDR-202 vs *Rahul S.* in RTO-019).
            </p>
            <div style="background: rgba(0,0,0,0.3); border: 1px dashed rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #34d399;">
                ✓ Phonetic Match (94%) &nbsp;|&nbsp; ✓ Phone Match (+91 98765...) &nbsp;|&nbsp; ✓ Vehicle Match (MH12AB1234)<br>
                <b>Match Score: 97%</b> ➔ Unifies under Entity ID: <b style="color: #00e5ff;">ENT-001</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # USP 4
        st.markdown("""
        <div class="usp-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">USP 04</span>
                <h4 style="margin: 0; color: #ffffff;">Cross-Case Link Discovery</h4>
            </div>
            <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;">
                Uncovers hidden connections between separate FIRs that individual station officers wouldn't normally correlate in isolation.
            </p>
            <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 8px; padding: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #f87171;">
                🚨 <b>Cross-Case Discovery</b>:<br>
                Case FIR-104 (Kothrud) ──► [Shared Vehicle: MH12AB1234] ◄── Case FIR-087 (Swargate)
            </div>
        </div>
        """, unsafe_allow_html=True)

        # USP 6
        st.markdown("""
        <div class="usp-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="background: rgba(0, 229, 255, 0.15); color: #00e5ff; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">USP 06</span>
                <h4 style="margin: 0; color: #ffffff;">Explainable Investigation Priority</h4>
            </div>
            <p style="color: #94a3b8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;">
                Ranks leads using an explainable priority index ($87/100$) rather than opaque black-box "criminality scores", with strict evidentiary disclaimers.
            </p>
            <div style="background: rgba(0,0,0,0.3); border: 1px dashed rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #fbbf24;">
                Connectivity: 30/35 | Cross-Case: 25/25 | Transactions: 18/20 | Evidence: 14/20 = <b>87/100</b><br>
                <span style="font-size: 0.7rem; color: #94a3b8;">*Notice: Investigation Priority is a dispatch heuristic and does not establish legal guilt.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-top: 1px solid rgba(0, 229, 255, 0.2); margin: 25px 0;'>", unsafe_allow_html=True)

    # 4. Hero Demonstration Walkthrough
    st.markdown("""
    <div style="background: rgba(13, 21, 39, 0.8); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 14px; padding: 24px; margin-bottom: 30px;">
        <h3 style="margin: 0 0 12px 0; color: #00e5ff;">🎬 The 60-Second Hero Demonstration Flow</h3>
        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6; margin-bottom: 18px;">
            For hackathon evaluation, test the deeply interconnected <b>Case FIR-104 (Kothrud Vehicle &amp; Electronics Theft)</b>:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
            <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                <b style="color: #00e5ff;">Step 1 — Login</b><br>
                <span style="font-size: 0.8rem; color: #94a3b8;">Access with 1-Click Demo Credentials as PI Vikram Patil.</span>
            </div>
            <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                <b style="color: #00e5ff;">Step 2 — Data Hub</b><br>
                <span style="font-size: 0.8rem; color: #94a3b8;">Examine ingested FIR, CDR, ANPR, and Financial data.</span>
            </div>
            <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                <b style="color: #00e5ff;">Step 3 — Resolution</b><br>
                <span style="font-size: 0.8rem; color: #94a3b8;">Resolve duplicate record <i>Rahul Sharm</i> into <i>ENT-001</i>.</span>
            </div>
            <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                <b style="color: #00e5ff;">Step 4 — Graph &amp; Cross-Case</b><br>
                <span style="font-size: 0.8rem; color: #94a3b8;">Surface vehicle MH12AB1234 linking FIR-104 &amp; FIR-087.</span>
            </div>
            <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 8px; padding: 12px;">
                <b style="color: #00e5ff;">Step 5 — Query &amp; Report</b><br>
                <span style="font-size: 0.8rem; color: #94a3b8;">Ask CrimeLens &amp; download structured police report.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
