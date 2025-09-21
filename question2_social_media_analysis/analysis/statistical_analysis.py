import pandas as pd
import scipy.stats as stats

def analyze_books(input_file="./src/data_collection/data/cleaned_books.csv"):
    df = pd.read_csv(input_file)

    # Clean Price column
    df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace('[\$,]', '', regex=True), errors='coerce')
    df = df.dropna(subset=['Price'])

    print("Descriptive Statistics:")
    print(df["Price"].describe())
    print(df["Rating"].value_counts())

    # Correlation between Price and Rating
    corr = df["Price"].corr(df["Rating"])
    print(f"\n🔗 Correlation (Price vs Rating): {corr:.2f}")

    # Hypothesis test: compare average price of rating=5 vs rating=3
    group1 = df[df["Rating"] == 5]["Price"]
    group2 = df[df["Rating"] == 3]["Price"]
    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False, nan_policy="omit")

    print(f"\nHypothesis Test (Rating 5 vs 3): t={t_stat:.2f}, p={p_val:.4f}")

def main():
    analyze_books()

if __name__ == "__main__":
    main()
