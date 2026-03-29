import streamlit as st
import pandas as pd

from src.data_loader import preprocess_data
from src.optimizer import assign_deliveries

st.set_page_config(page_title="Delivery Optimizer", layout="wide")

st.title("🚚 Delivery Optimization Dashboard")

uploaded_file = st.file_uploader("Upload Delivery CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.dataframe(df.head())

    # Preprocess
    df = preprocess_data(df)

    # Assign
    agents = assign_deliveries(df)

    # Prepare outputs
    plan_rows = []
    summary_rows = []

    for agent, details in agents.items():
        for task in details["tasks"]:
            plan_rows.append([
                agent,
                task["LocationID"],
                task["Product"],
                task["Priority"],
                task["Distance"]
            ])

        summary_rows.append([agent, details["total_distance"]])

    plan_df = pd.DataFrame(plan_rows, columns=[
        "Agent", "LocationID", "Product", "Priority", "Distance"
    ])

    summary_df = pd.DataFrame(summary_rows, columns=[
        "Agent", "TotalDistance"
    ])

    st.subheader("📦 Delivery Plan")
    st.dataframe(plan_df)

    st.subheader("📈 Agent Workload")
    st.bar_chart(summary_df.set_index("Agent"))