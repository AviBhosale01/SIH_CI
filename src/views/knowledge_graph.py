"""
CrimeLens - Interactive Knowledge Graph Workspace
Visualizes multi-entity relational networks (Persons, Vehicles, Phones, Cases, Transactions),
side-panel dossier inspection, and in-graph natural language query answering.
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import networkx as nx
from src.core.synthetic_data import DEMO_ENTITIES, DEMO_CASES
from src.utils.styles import render_html

def render_knowledge_graph_view():
    """
    Render CrimeLens Knowledge Graph with interactive node selection,
    in-graph query execution, and detailed evidence-backed dossiers.
    """
    st.markdown("## 🕸️ Investigation Knowledge Graph Workspace")
    st.write("Dynamic multi-entity relationship graph linking suspects, vehicles, phones, transactions, and crime scenes across cases.")

    active_case_id = st.session_state.get("active_case_id", "FIR-104")

    # 1. IN-GRAPH QUERY SEARCH BAR ("Ask on the Spot")
    render_html("""
    <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 229, 255, 0.3); border-radius: 12px; padding: 16px; margin-bottom: 20px;">
        <div style="font-size: 0.85rem; font-weight: 800; color: #00e5ff; text-transform: uppercase; margin-bottom: 6px; font-family: 'JetBrains Mono', monospace;">
            🔍 In-Graph Evidence Query &amp; Reasoning
        </div>
        <div style="font-size: 0.82rem; color: #94a3b8; margin-bottom: 10px;">
            Ask questions directly about entities, cross-case connections, or transactions:
        </div>
    </div>
    """)

    q_col1, q_col2, q_col3 = st.columns(3)
    preset_query = None
    with q_col1:
        if st.button("❓ How many connections does Rahul Sharma have?", key="btn_q_rahul_conn"):
            preset_query = "connections_rahul"
    with q_col2:
        if st.button("🚗 What connects Case FIR-104 and FIR-087?", key="btn_q_cross_case"):
            preset_query = "cross_case_104_087"
    with q_col3:
        if st.button("💳 Show unusual financial transactions", key="btn_q_finances"):
            preset_query = "unusual_finances"

    custom_graph_search = st.text_input("Or enter an investigation query...", placeholder="e.g. How is Rahul Sharma connected to Case 087?", key="txt_graph_query")

    if preset_query == "connections_rahul" or "rahul" in custom_graph_search.lower():
        render_html("""
        <div style="background: rgba(0, 229, 255, 0.08); border-left: 4px solid #00e5ff; border: 1px solid rgba(0, 229, 255, 0.3); border-left-width: 4px; border-radius: 8px; padding: 16px; margin-bottom: 18px;">
            <div style="font-weight: 800; color: #00e5ff; font-size: 1.05rem; margin-bottom: 8px;">
                Investigation Result: Rahul Sharma (ENT-001) has 4 primary verified connections
            </div>
            <div style="color: #f1f5f9; font-size: 0.88rem; line-height: 1.6;">
                1. 👤 <b>Amit Verma (ENT-002)</b> — Co-associate linked via <b>14 high-frequency CDR calls</b> in 48h <i>[Evidence: CDR-202]</i><br>
                2. 🚗 <b>White Swift MH12AB1234 (ENT-003)</b> — Registered personal vehicle spotted at crime scenes <i>[Evidence: VEH-019 / RTO]</i><br>
                3. 💳 <b>Transaction TXN-203 (ENT-006)</b> — Direct ₹75,000 IMPS fund transfer sent to Amit Verma <i>[Evidence: FIN-203]</i><br>
                4. 📁 <b>Case FIR-087 (Swargate)</b> — Cross-case linkage via vehicle presence at warehouse burglary <i>[Evidence: FIR-087 / CCTV]</i>
            </div>
        </div>
        """)

    elif preset_query == "cross_case_104_087" or ("104" in custom_graph_search and "087" in custom_graph_search):
        render_html("""
        <div style="background: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; border: 1px solid rgba(239, 68, 68, 0.35); border-left-width: 4px; border-radius: 8px; padding: 16px; margin-bottom: 18px;">
            <div style="font-weight: 800; color: #f87171; font-size: 1.05rem; margin-bottom: 8px;">
                🚨 Critical Cross-Case Connection Detected: Case FIR-104 ⟷ Case FIR-087
            </div>
            <div style="color: #f1f5f9; font-size: 0.88rem; line-height: 1.6;">
                <b>Connecting Asset:</b> Vehicle <b>MH12AB1234</b> (White Maruti Suzuki Swift)<br>
                • <b>Case FIR-104 (Kothrud)</b>: Vehicle spotted at parking complex during electronics theft on 12 Aug 2026.<br>
                • <b>Case FIR-087 (Swargate)</b>: Same vehicle identified on CCTV as the getaway transport for warehouse burglary on 10 Aug 2026.<br>
                • <b>Registered Owner</b>: Rahul Sharma (ENT-001)<br>
                <b>Evidence Audit Trail:</b> <span style="color: #00e5ff; font-family: 'JetBrains Mono', monospace;">[FIR-104] [FIR-087] [VEH-019] [ANPR-SWG-04]</span>
            </div>
        </div>
        """)

    elif preset_query == "unusual_finances" or "transaction" in custom_graph_search.lower() or "financial" in custom_graph_search.lower():
        render_html("""
        <div style="background: rgba(245, 158, 11, 0.1); border-left: 4px solid #f59e0b; border: 1px solid rgba(245, 158, 11, 0.35); border-left-width: 4px; border-radius: 8px; padding: 16px; margin-bottom: 18px;">
            <div style="font-weight: 800; color: #fbbf24; font-size: 1.05rem; margin-bottom: 8px;">
                ⚠️ Suspicious Financial Event: TXN-203 (₹75,000 Payout)
            </div>
            <div style="color: #f1f5f9; font-size: 0.88rem; line-height: 1.6;">
                • <b>Sender:</b> Rahul Sharma &nbsp;|&nbsp; <b>Recipient:</b> Amit Verma<br>
                • <b>Timing:</b> Executed 26 hours following incident FIR-104 on 13 Aug 2026 at 14:22 IST.<br>
                • <b>Channel:</b> IMPS Transfer tagged 'Auto Parts Settlement'.<br>
                <b>Evidence Audit Trail:</b> <span style="color: #00e5ff; font-family: 'JetBrains Mono', monospace;">[FIN-203] [HDFC-STMT-992]</span>
            </div>
        </div>
        """)

    # 2. GRAPH FILTERS & CONTROLS
    st.markdown("##### ⚙️ Graph Filtering & Scope")
    f_col1, f_col2, f_col3 = st.columns([1.5, 1.5, 1])
    with f_col1:
        filter_types = st.multiselect(
            "Filter Entity Node Types",
            ["PERSON", "VEHICLE", "PHONE", "LOCATION", "CASE", "TRANSACTION"],
            default=["PERSON", "VEHICLE", "PHONE", "LOCATION", "CASE", "TRANSACTION"]
        )
    with f_col2:
        filter_rels = st.multiselect(
            "Filter Relationship Edges",
            ["CONTACTED", "OWNS", "USED", "TRANSFERRED", "LOCATED_AT", "INVOLVED_IN"],
            default=["CONTACTED", "OWNS", "USED", "TRANSFERRED", "LOCATED_AT", "INVOLVED_IN"]
        )
    with f_col3:
        highlight_case = st.selectbox("Highlight Case Cluster", ["All Cases", "FIR-104", "FIR-087", "FIR-052"])

    # 3. KNOWLEDGE GRAPH CANVAS + SIDE-PANEL DOSSIER
    col_graph, col_dossier = st.columns([2.3, 1.2])

    with col_graph:
        # Build NetworkX graph
        G = nx.Graph()

        # Nodes setup
        node_definitions = [
            ("Rahul Sharma", {"type": "PERSON", "id": "ENT-001", "color": "#3b82f6", "size": 32}),
            ("Amit Verma", {"type": "PERSON", "id": "ENT-002", "color": "#3b82f6", "size": 28}),
            ("MH12AB1234", {"type": "VEHICLE", "id": "ENT-003", "color": "#f59e0b", "size": 30}),
            ("+91 98765 43210", {"type": "PHONE", "id": "ENT-004", "color": "#10b981", "size": 22}),
            ("+91 98230 11223", {"type": "PHONE", "id": "ENT-005", "color": "#10b981", "size": 22}),
            ("TXN-203 (₹75k)", {"type": "TRANSACTION", "id": "ENT-006", "color": "#06b6d4", "size": 24}),
            ("Kothrud Scene", {"type": "LOCATION", "id": "ENT-007", "color": "#8b5cf6", "size": 24}),
            ("Swargate Hub", {"type": "LOCATION", "id": "ENT-008", "color": "#8b5cf6", "size": 24}),
            ("Case FIR-104", {"type": "CASE", "id": "FIR-104", "color": "#ef4444", "size": 35}),
            ("Case FIR-087", {"type": "CASE", "id": "FIR-087", "color": "#ef4444", "size": 35})
        ]

        for name, data in node_definitions:
            if data["type"] in filter_types:
                G.add_node(name, **data)

        # Edges setup
        edge_definitions = [
            ("Rahul Sharma", "Amit Verma", {"rel": "CONTACTED", "label": "14 CDR Calls"}),
            ("Rahul Sharma", "MH12AB1234", {"rel": "OWNS", "label": "Owner / Uses"}),
            ("Rahul Sharma", "+91 98765 43210", {"rel": "USED", "label": "Subscriber"}),
            ("Amit Verma", "+91 98230 11223", {"rel": "USED", "label": "Subscriber"}),
            ("Rahul Sharma", "TXN-203 (₹75k)", {"rel": "TRANSFERRED", "label": "Sender"}),
            ("TXN-203 (₹75k)", "Amit Verma", {"rel": "TRANSFERRED", "label": "Receiver"}),
            ("Rahul Sharma", "Case FIR-104", {"rel": "INVOLVED_IN", "label": "Prime Suspect"}),
            ("MH12AB1234", "Case FIR-104", {"rel": "INVOLVED_IN", "label": "Suspect Vehicle"}),
            ("MH12AB1234", "Case FIR-087", {"rel": "INVOLVED_IN", "label": "Getaway Vehicle"}),
            ("Rahul Sharma", "Kothrud Scene", {"rel": "LOCATED_AT", "label": "Present"}),
            ("Amit Verma", "Swargate Hub", {"rel": "LOCATED_AT", "label": "Present"}),
            ("Case FIR-087", "Swargate Hub", {"rel": "LOCATED_AT", "label": "Location"})
        ]

        for u, v, data in edge_definitions:
            if G.has_node(u) and G.has_node(v) and data["rel"] in filter_rels:
                G.add_edge(u, v, **data)

        # Fixed pleasant spring layout
        pos = nx.spring_layout(G, seed=42, k=1.2)

        edge_x = []
        edge_y = []
        edge_texts = []
        for edge in G.edges(data=True):
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1.8, color='rgba(0, 229, 255, 0.45)'),
            hoverinfo='none',
            mode='lines'
        )

        node_x = []
        node_y = []
        node_colors = []
        node_sizes = []
        node_texts = []
        node_hover = []

        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            n_data = G.nodes[node]
            node_colors.append(n_data.get("color", "#3b82f6"))
            node_sizes.append(n_data.get("size", 25))
            node_texts.append(node)
            node_hover.append(f"<b>{node}</b><br>Type: {n_data.get('type')}<br>ID: {n_data.get('id')}")

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_texts,
            textposition="top center",
            hovertext=node_hover,
            marker=dict(
                color=node_colors,
                size=node_sizes,
                line=dict(width=2, color='#ffffff')
            ),
            textfont=dict(color="#e2e8f0", size=10, family="Plus Jakarta Sans")
        )

        fig_graph = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title=dict(text="Investigation Knowledge Graph (Visual Network Links)", font=dict(color="#ffffff", size=14)),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=10, l=10, r=10, t=35),
                paper_bgcolor="rgba(10, 15, 29, 0.95)",
                plot_bgcolor="rgba(10, 15, 29, 0.95)",
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                height=520
            )
        )

        st.plotly_chart(fig_graph, use_container_width=True, config={'scrollZoom': True, 'displayModeBar': False})

    with col_dossier:
        st.markdown("### 📋 Entity Dossier Inspector")
        st.write("Inspect detailed personality, criminal links, and evidence sources:")

        entity_names = [e["name"] for e in DEMO_ENTITIES]
        selected_inspect_name = st.selectbox("Select Entity to Inspect", entity_names, index=0)
        sel_entity = next((e for e in DEMO_ENTITIES if e["name"] == selected_inspect_name), DEMO_ENTITIES[0])

        e_type = sel_entity.get("type", "PERSON")
        e_color = "#3b82f6" if e_type == "PERSON" else ("#f59e0b" if e_type == "VEHICLE" else "#10b981")

        render_html(f"""
        <div style="background: rgba(13, 21, 39, 0.9); border: 1px solid rgba(0, 229, 255, 0.3); border-radius: 12px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="background: {e_color}22; color: {e_color}; border: 1px solid {e_color}; font-size: 0.75rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;">{e_type}</span>
                <span style="color: #00e5ff; font-weight: 800; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;">{sel_entity['id']}</span>
            </div>
            <h3 style="margin: 0 0 6px 0; color: #ffffff; font-size: 1.3rem;">{sel_entity['name']}</h3>
            
            <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.7; margin-top: 10px;">
                <b>Linked Cases:</b> <span style="color: #ef4444; font-weight: 700;">{", ".join(sel_entity['cases'])}</span><br>
                <b>Phone:</b> {sel_entity.get('phone', 'N/A')}<br>
                <b>Vehicle:</b> {sel_entity.get('vehicle', 'N/A')}<br>
                <b>Location:</b> {sel_entity.get('location', 'Pune')}<br>
            </div>

            <hr style="border-top: 1px solid rgba(75, 85, 99, 0.3); margin: 10px 0;">

            <div style="font-size: 0.8rem; color: #94a3b8;">
                <b>Evidentiary Records:</b><br>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                    <span style="background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">[FIR-104]</span>
                    <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">[CDR-202]</span>
                    <span style="background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">[VEH-019]</span>
                    <span style="background: rgba(6, 182, 212, 0.2); color: #22d3ee; border: 1px solid #06b6d4; padding: 2px 6px; border-radius: 4px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace;">[FIN-203]</span>
                </div>
            </div>
        </div>
        """)
