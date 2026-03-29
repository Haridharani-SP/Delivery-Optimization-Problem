import pandas as pd
import os


def save_outputs(agents, output_dir="output"):
    """
    Save delivery plan and summary as CSV
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plan_rows = []
    summary_rows = []

    for agent, details in agents.items():
        total_distance = details["total_distance"]

        for task in details["tasks"]:
            plan_rows.append([
                agent,
                task["LocationID"],
                task["Product"],
                task["Priority"],
                task["Distance"]
            ])

        summary_rows.append([agent, total_distance])

    plan_df = pd.DataFrame(plan_rows, columns=[
        "Agent", "LocationID", "Product", "Priority", "Distance"
    ])

    summary_df = pd.DataFrame(summary_rows, columns=[
        "Agent", "TotalDistance"
    ])

    # Save files
    plan_df.to_csv(f"{output_dir}/delivery_plan.csv", index=False)
    summary_df.to_csv(f"{output_dir}/agent_summary.csv", index=False)

    return plan_df, summary_df