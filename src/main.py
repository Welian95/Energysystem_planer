import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
from streamlit_flow.state import StreamlitFlowState
from uuid import uuid4
from streamlit_flow.layouts import TreeLayout

# Titel der App
st.title("Energiesystem Planer")
st.write("Nutzen Sie die Bausteine (Sources, Sinks, Transformers, Storages), um Ihr Energiesystem zu erstellen.")

# Initialisieren des Zustands, falls nicht vorhanden
if 'flow_state' not in st.session_state:
    nodes = [
        # Beispiel-Nodes zum Start
        StreamlitFlowNode(id=str(uuid4()), pos=(50, 50), data={'content': 'Source 1'}, node_type='default', source_position='right'),
        StreamlitFlowNode(id=str(uuid4()), pos=(50, 50), data={'content': 'Sink 1'}, node_type='default', target_position='left')
    ]
    edges = []
    st.session_state.flow_state = StreamlitFlowState(nodes, edges)

st.write("Zum hinzufügen oder löschen von Element im Diagramm Rechts klick ins Diagramm")

new_state = streamlit_flow(
    'fully_interactive_flow',
    st.session_state.flow_state,  # Start with the existing state
    fit_view=True,
    show_controls=True,
    allow_new_edges=True,
    animate_new_edges=True,


layout=TreeLayout("right"),
    enable_pane_menu=True,
    enable_edge_menu=True,
    enable_node_menu=True
)

# Aktualisiere den Zustand
st.session_state.flow_state = new_state


# Node-Liste anzeigen
st.sidebar.write("## Aktuelle Nodes")
for node in st.session_state.flow_state.nodes:
    st.sidebar.write(f"{node.data['content']}")

# Edge-Liste anzeigen
st.sidebar.write("## Aktuelle Verbindungen")
for edge in st.session_state.flow_state.edges:
    source_node = next((node for node in st.session_state.flow_state.nodes if node.id == edge.source), None)
    target_node = next((node for node in st.session_state.flow_state.nodes if node.id == edge.target), None)
    if source_node and target_node:
        st.sidebar.write(f"{source_node.data['content']} -> {target_node.data['content']}")