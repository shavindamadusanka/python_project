import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def visualize_books(input_file="./src/data_collection/data/cleaned_books.csv"):
    df = pd.read_csv(input_file)

    # Price distribution
    plt.hist(df["Price"], bins=20, edgecolor="black")
    plt.title("Price Distribution")
    plt.xlabel("Price (£)")
    plt.ylabel("Count")
    plt.show()

    # Boxplot by rating
    sns.boxplot(x="Rating", y="Price", data=df)
    plt.title("Price vs Rating")
    plt.show()

    # Scatter (Price vs Rating)
    sns.scatterplot(x="Rating", y="Price", data=df)
    plt.title("Price vs Rating Scatter")
    plt.show()

    # Interactive plot with Plotly
    fig = px.scatter(df, x="Rating", y="Price", hover_data=["Title"], title="Interactive Price vs Rating")
    fig.show()

def main():
    visualize_books()

if __name__ == "__main__":
    main()
