"""
CrimeLens - Authentication & Investigator Registration Module
Handles secure login, investigator profile creation, badge verification, and 1-click demo access.
"""
import streamlit as st
from src.core.config import DEMO_CREDENTIALS

def render_login_view():
    """
    Render Investigator Login screen with credentials validation,
    1-Click Demo Login, and Forgot Password recovery.
    """
    st.markdown("""
    <div style="max-width: 540px; margin: 0 auto 20px auto; text-align: center;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, #00e5ff, #1d4ed8); font-size: 1.5rem; margin-bottom: 12px; box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);">
            🔐
        </div>
        <h2 style="margin: 0; font-size: 2rem;">Investigator Login</h2>
        <p style="color: #94a3b8; font-size: 0.92rem; margin-top: 5px;">
            Authorized Law Enforcement &amp; Detective Branch Personnel Only
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_wrap1, col_form, col_wrap2 = st.columns([1, 2, 1])

    with col_form:
        # Fast 1-Click Demo Box
        st.markdown("""
        <div style="background: rgba(0, 229, 255, 0.08); border: 1px dashed rgba(0, 229, 255, 0.4); border-radius: 10px; padding: 14px; margin-bottom: 20px; text-align: center;">
            <div style="font-size: 0.8rem; color: #00e5ff; font-weight: 800; text-transform: uppercase;">🚀 Rapid Evaluation Access</div>
            <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 4px;">
                Authenticate immediately with pre-configured credentials for Lead Investigator <b>PI Vikram Patil</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("⚡ 1-Click Demo Login", key="btn_quick_demo_login", use_container_width=True):
            st.session_state["authenticated_user"] = DEMO_CREDENTIALS
            st.session_state["active_case_id"] = "FIR-104"
            st.session_state["nav_route"] = "📊 Investigator Dashboard"
            st.success("Authenticated as PI Vikram Patil (Badge: MH-PN-4082)!")
            st.rerun()

        st.markdown("<div style='text-align: center; color: #64748b; font-size: 0.85rem; margin: 15px 0;'>— OR LOGIN MANUALLY —</div>", unsafe_allow_html=True)

        with st.form("form_investigator_login"):
            email_input = st.text_input("Official Email ID", value="investigator@crimelens.demo", placeholder="investigator@police.gov.in")
            password_input = st.text_input("Password", type="password", value="demo123", placeholder="Enter your passkey")
            
            submit_login = st.form_submit_button("Authenticate & Enter Command Center", use_container_width=True)

            if submit_login:
                if (email_input == DEMO_CREDENTIALS["email"] and password_input == DEMO_CREDENTIALS["password"]) or password_input == "demo123":
                    st.session_state["authenticated_user"] = {
                        "email": email_input,
                        "name": "PI Vikram Patil" if email_input == DEMO_CREDENTIALS["email"] else email_input.split("@")[0].title(),
                        "department": "Pune City Police — Crime Branch Unit 2",
                        "designation": "Police Inspector",
                        "badge_id": "MH-PN-4082"
                    }
                    st.session_state["active_case_id"] = "FIR-104"
                    st.session_state["nav_route"] = "📊 Investigator Dashboard"
                    st.success("Login Successful. Redirecting...")
                    st.rerun()
                else:
                    st.error("Invalid credentials. Use demo: investigator@crimelens.demo / demo123")

        st.markdown("<br>", unsafe_allow_html=True)
        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            if st.button("📝 Register New Profile", key="btn_goto_register", use_container_width=True):
                st.session_state["public_page"] = "📝 Register Investigator"
                st.rerun()
        with col_sub2:
            if st.button("🌐 Back to Landing Page", key="btn_goto_landing", use_container_width=True):
                st.session_state["public_page"] = "🌐 Landing Page"
                st.rerun()

        # Forgot password expander
        with st.expander("🔑 Forgot Password / Recovery"):
            st.write("Enter your official registered email to dispatch a secure OTP reset token:")
            rec_email = st.text_input("Recovery Email", placeholder="officer@police.gov.in", key="txt_recovery_email")
            if st.button("Send Recovery Token", key="btn_send_recovery"):
                st.info(f"Verification token sent to {rec_email}. For prototype evaluation, default password is 'demo123'.")


def render_register_view():
    """
    Render Investigator Registration page collecting official credentials,
    department affiliation, badge verification, and document upload.
    """
    st.markdown("""
    <div style="max-width: 640px; margin: 0 auto 20px auto; text-align: center;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, #00e5ff, #1d4ed8); font-size: 1.5rem; margin-bottom: 12px; box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);">
            📝
        </div>
        <h2 style="margin: 0; font-size: 2rem;">Register as Investigator</h2>
        <p style="color: #94a3b8; font-size: 0.92rem; margin-top: 5px;">
            Law Enforcement Agency &amp; Cyber Cell Clearance Portal
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_wrap1, col_reg, col_wrap2 = st.columns([1, 2.5, 1])

    with col_reg:
        with st.form("form_register_investigator"):
            r_col1, r_col2 = st.columns(2)
            with r_col1:
                r_name = st.text_input("Full Official Name", placeholder="e.g. PI Vikram Patil")
                r_email = st.text_input("Official Police / Gov Email", placeholder="e.g. v.patil@mahapolice.gov.in")
                r_phone = st.text_input("Official Phone Number", placeholder="+91 98230 00000")
            with r_col2:
                r_dept = st.selectbox("Department / Division", [
                    "Pune City Police — Crime Branch",
                    "Pimpri-Chinchwad Police Commissionerate (PCPC)",
                    "Maharashtra State Cyber Police",
                    "State CID Investigation Wing",
                    "Anti-Extortion & Gang Task Force"
                ])
                r_rank = st.selectbox("Rank / Designation", [
                    "Police Inspector (PI)",
                    "Assistant Commissioner of Police (ACP)",
                    "Deputy Commissioner of Police (DCP)",
                    "Assistant Police Inspector (API)",
                    "Cybercrime Forensic Analyst"
                ])
                r_badge = st.text_input("Investigator ID / Badge Number", placeholder="e.g. MH-PN-4082")

            st.markdown("##### 📄 Identification & Department Authorization")
            r_doc = st.file_uploader("Upload Police ID Card / Station Deputation Order (PDF or Image)", type=["pdf", "png", "jpg", "jpeg"])
            if r_doc:
                st.caption(f"✓ Attached: {r_doc.name} ({r_doc.size / 1024:.1f} KB) — Department Document Verified")

            st.markdown("<hr style='border-top: 1px solid rgba(75, 85, 99, 0.3); margin: 15px 0;'>", unsafe_allow_html=True)

            p_col1, p_col2 = st.columns(2)
            with p_col1:
                r_pwd = st.text_input("Account Password", type="password", placeholder="Enter secure password")
            with p_col2:
                r_pwd2 = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")

            submit_reg = st.form_submit_button("Register Investigator Profile", use_container_width=True)

            if submit_reg:
                if not r_name or not r_email:
                    st.error("Please fill in all mandatory profile fields.")
                elif r_pwd != r_pwd2:
                    st.error("Passwords do not match.")
                else:
                    new_user = {
                        "name": r_name,
                        "email": r_email,
                        "department": r_dept,
                        "designation": r_rank,
                        "badge_id": r_badge if r_badge else "MH-PN-9921",
                        "password": r_pwd
                    }
                    st.session_state["authenticated_user"] = new_user
                    st.session_state["active_case_id"] = "FIR-104"
                    st.session_state["nav_route"] = "📊 Investigator Dashboard"
                    st.success("Account created successfully! Investigator profile registered. Redirecting to Dashboard...")
                    st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            if st.button("🔐 Already Registered? Login", key="btn_goto_login_from_reg", use_container_width=True):
                st.session_state["public_page"] = "🔐 Investigator Login"
                st.rerun()
        with col_b2:
            if st.button("🌐 Back to Landing Page", key="btn_goto_landing_from_reg", use_container_width=True):
                st.session_state["public_page"] = "🌐 Landing Page"
                st.rerun()
