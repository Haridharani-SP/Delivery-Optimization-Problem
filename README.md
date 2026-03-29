# 🚚 Delivery Optimization System

## 📌 Objective
To assign delivery tasks efficiently among multiple agents while:
- Prioritizing urgent deliveries
- Minimizing total travel distance
- Ensuring balanced workload

---

## 🧠 Approach

1. Load dataset using pandas
2. Convert priority levels:
   - High → 3
   - Medium → 2
   - Low → 1
3. Sort deliveries:
   - Priority (descending)
   - Distance (ascending)
4. Use greedy load balancing:
   - Assign each delivery to the agent with the least total distance

---

## 📁 Project Structure

- `data/` → Input dataset
- `src/` → Core logic (data loading, optimization, utils)
- `app/` → Streamlit UI
- `output/` → Generated results

---

## ▶️ How to Run

### Run Backend:
```bash
python main.py
```

### Run Streamlit App:
```bash
streamlit run app/streamlit_app.py
```

---

## 📊 Outputs

- `delivery_plan.csv` → Delivery assignments
- `agent_summary.csv` → Total distance per agent

---

## 💡 Key Highlights

- Greedy optimization algorithm
- Balanced workload distribution
- Modular and clean code structure
- Interactive visualization using Streamlit

---

## 🚀 Future Improvements

- Route optimization using TSP
- Real-time traffic integration
- AI-based priority prediction
- Map-based visualization

---

## 🧠 Insight

This solution uses a greedy strategy to achieve near-optimal load balancing efficiently, making it practical for real-world logistics systems.