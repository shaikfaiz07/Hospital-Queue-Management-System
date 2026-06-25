import streamlit as st
import pandas as pd

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Hospital Queue Management System",
    page_icon="🏥",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1 {
    color: #0066cc;
    text-align: center;
}

.stButton>button {
    width: 100%;
    background-color: #0066cc;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Session State
# ----------------------------
if "queue" not in st.session_state:
    st.session_state.queue = []

# ----------------------------
# Title
# ----------------------------
st.title("🏥 Hospital Queue Management System")
st.markdown("---")

# ----------------------------
# Sidebar
# ----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["➕ Add Patient", "📋 View Queue", "👨‍⚕️ Treat Patient"]
)

# ----------------------------
# Dashboard Metrics
# ----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Patients Waiting", len(st.session_state.queue))

with col2:
    emergency_count = len(
        [p for p in st.session_state.queue if p["priority"] == 1]
    )
    st.metric("🚨 Emergency Cases", emergency_count)

with col3:
    st.metric("🏥 Departments", 3)

st.markdown("---")

# ============================
# ADD PATIENT
# ============================
if menu == "➕ Add Patient":

    st.subheader("Add New Patient")

    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )

    token = st.number_input(
        "Token Number",
        min_value=1,
        step=1
    )

    priority = st.selectbox(
        "Priority Level",
        [
            1,
            2,
            3,
            4
        ]
    )

    department = st.selectbox(
        "Department",
        [
            "ICU",
            "OPD",
            "General"
        ]
    )

    if st.button("Add Patient"):

        patient = {
            "name": name,
            "age": age,
            "token": token,
            "priority": priority,
            "department": department
        }

        st.session_state.queue.append(patient)

        st.session_state.queue.sort(
            key=lambda x: x["priority"]
        )

        st.success(f"✅ {name} added successfully!")

# ============================
# VIEW QUEUE
# ============================
elif menu == "📋 View Queue":

    st.subheader("Current Patient Queue")

    if st.session_state.queue:

        df = pd.DataFrame(st.session_state.queue)

        df.columns = [
            "Name",
            "Age",
            "Token",
            "Priority",
            "Department"
        ]

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("Queue is empty.")

# ============================
# TREAT PATIENT
# ============================
elif menu == "👨‍⚕️ Treat Patient":

    st.subheader("Treat Patient")

    if st.session_state.queue:

        next_patient = st.session_state.queue[0]

        st.info(
            f"""
            Next Patient:
            
            Name: {next_patient['name']}
            
            Department: {next_patient['department']}
            
            Priority: {next_patient['priority']}
            """
        )

        if st.button("Treat Now"):

            treated = st.session_state.queue.pop(0)

            st.success(
                f"✅ Patient Treated: {treated['name']}"
            )

    else:
        st.warning("No patients waiting.")