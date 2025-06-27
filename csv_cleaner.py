import pandas as pd
import os

def clean_csv(file_path, output_name=None):
    try:
        print("\n📂 Loading file...")
        df = pd.read_csv(file_path)

        original_shape = df.shape
        print(f"✅ Original shape: {original_shape}")

        # Remove fully empty rows
        df.dropna(how='all', inplace=True)

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Replace common invalid values
        df.replace(["?", "N/A", "null", "none", "None", "--"], pd.NA, inplace=True)

        # Fill missing values
        df.fillna("N/A", inplace=True)

        # Attempt to convert any column to datetime if possible
        for col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except (ValueError, TypeError):
                continue

        # Save output
        cleaned_file = output_name if output_name else "cleaned_" + os.path.basename(file_path)
        df.to_csv(cleaned_file, index=False)

        print(f"\n📊 Cleaned file saved as: {cleaned_file}")
        print(f"📁 Saved in: {os.path.abspath(cleaned_file)}")
        print(f"🔍 Final shape: {df.shape}")
        print("🧼 Cleaning complete!")

    except Exception as e:
        print("❌ Error:", e)


# ==== User Interface ====
if __name__ == "__main__":
    print("🔧 CSV Cleaner Pro 🔧")
    path = input("📥 Enter path to your CSV file: ")
    name = input("💾 Enter output filename (or leave blank for auto-name): ")

    clean_csv(path, name if name else None)
