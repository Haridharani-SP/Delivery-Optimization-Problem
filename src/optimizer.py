def assign_deliveries(df, num_agents=3):
    """
    Assign deliveries using greedy load balancing
    """
    agents = {
        f"Agent_{i+1}": {
            "tasks": [],
            "total_distance": 0
        }
        for i in range(num_agents)
    }

    for _, row in df.iterrows():
        # Find agent with minimum workload
        selected_agent = min(
            agents,
            key=lambda x: agents[x]["total_distance"]
        )

        task = {
            "LocationID": row["LocationID"],
            "Product": row["Product_Name"],
            "Priority": row["Priority"],
            "Distance": row["Distance"]
        }

        agents[selected_agent]["tasks"].append(task)
        agents[selected_agent]["total_distance"] += row["Distance"]

    return agents