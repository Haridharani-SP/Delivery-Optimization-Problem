from src.data_loader import load_data, preprocess_data
from src.optimizer import assign_deliveries
from src.utils import save_outputs


def main():
    file_path = "./data/delivery_dataset_300_rows.csv"

    print("📥 Loading data...")
    df = load_data(file_path)

    print("🔄 Preprocessing data...")
    df = preprocess_data(df)

    print("⚙️ Assigning deliveries...")
    agents = assign_deliveries(df)

    print("💾 Saving results...")
    plan_df, summary_df = save_outputs(agents)

    print("\n✅ Delivery Plan Generated Successfully!\n")
    print(summary_df)


if __name__ == "__main__":
    main()