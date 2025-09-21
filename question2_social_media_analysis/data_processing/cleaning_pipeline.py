import pandas as pd

def clean_books(input_file="./src/data_collection/data/raw_books.csv",
                output_file="./src/data_collection/data/cleaned_books.csv"):
    df = pd.read_csv(input_file, encoding="utf-8")

    # Clean Price → remove symbols and convert to numeric
    df["Price"] = df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True)
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    # Normalize Rating → convert words to numbers
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["Rating"] = df["Rating"].map(rating_map)

    # Clean availability
    df["Availability"] = df["Availability"].str.extract(r"(\d+)").fillna(0).astype(int)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing ratings with 0
    df = df.fillna({"Rating": 0})

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_books()
    
def main():
    clean_books()