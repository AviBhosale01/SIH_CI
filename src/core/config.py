import streamlit as st
import os

# Application Identity & Branding
PAGE_TITLE = "CrimeLens — Crime Intelligence & Investigation Platform"
PAGE_ICON = "🔍"
TAGLINE = "Connect Evidence. Reveal Relationships. Accelerate Investigations."

# Default Demo Investigator Credentials
DEMO_CREDENTIALS = {
    "email": "investigator@crimelens.demo",
    "password": "demo123",
    "name": "PI Vikram Patil",
    "department": "Pune City Police — Crime Branch Unit 2",
    "designation": "Police Inspector / Lead Investigator",
    "badge_id": "MH-PN-4082"
}

# Supported Data Types for Data Intelligence Hub
DATA_SOURCES = [
    {"type": "FIR", "icon": "📄", "desc": "First Information Reports & Police Complaints"},
    {"type": "CDR", "icon": "📱", "desc": "Call Detail Records & Cell Tower Logs"},
    {"type": "FINANCIAL", "icon": "💳", "desc": "Bank Transfers, UPI & Account Statements"},
    {"type": "VEHICLE", "icon": "🚗", "desc": "RTO Records, CCTV & ANPR Sightings"},
    {"type": "INTELLIGENCE", "icon": "🕵️", "desc": "Informant Notes & Station Memos"}
]

# Entity Classifications & Visual Badges
ENTITY_TYPES = {
    "PERSON": {"color": "#3b82f6", "icon": "👤", "label": "Person / Suspect"},
    "VEHICLE": {"color": "#f59e0b", "icon": "🚗", "label": "Vehicle"},
    "PHONE": {"color": "#10b981", "icon": "📱", "label": "Phone / SIM"},
    "LOCATION": {"color": "#8b5cf6", "icon": "📍", "label": "Location / Scene"},
    "CASE": {"color": "#ef4444", "icon": "📁", "label": "Crime Case / FIR"},
    "TRANSACTION": {"color": "#06b6d4", "icon": "💳", "label": "Financial Transaction"},
    "ORGANIZATION": {"color": "#ec4899", "icon": "🏢", "label": "Gang / Entity Group"}
}

# Theme Colors & UI Palette (Cybersecurity Dark Theme)
THEME = {
    "bg_primary": "#0a0f1d",
    "bg_secondary": "#0f172a",
    "bg_card": "rgba(17, 24, 39, 0.90)",
    "border_glow": "rgba(0, 229, 255, 0.35)",
    "accent_cyan": "#00e5ff",
    "accent_blue": "#3b82f6",
    "danger_red": "#ef4444",
    "warning_amber": "#f59e0b",
    "success_emerald": "#10b981",
    "text_primary": "#ffffff",
    "text_muted": "#94a3b8"
}
