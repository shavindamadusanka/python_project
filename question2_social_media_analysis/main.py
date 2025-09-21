from data_collection.scrape_books import main as scrape_books_main
from data_collection.scrape_demo_sites import main as scrape_demo_sites_main
from data_collection.rss_parser import main as rss_parser_main
from data_processing.cleaning_pipeline import main as cleaning_pipeline_main
from analysis.statistical_analysis import main as statistical_analysis_main
from models.regression import main as regression_main
from visualizations.plots import main as plots_main

def main():
    print("Step 1: Data Collection - Books")
    scrape_books_main()
    print("Step 2: Data Collection - Demo Sites")
    scrape_demo_sites_main()
    print("Step 3: Data Collection - RSS Feed")
    rss_parser_main()

    print("Step 4: Data Cleaning")
    cleaning_pipeline_main()

    print("Step 5: Statistical Analysis")
    statistical_analysis_main()

    print("Step 6: Regression Modeling")
    regression_main()

    print("Step 7: Visualization")
    plots_main()

    print("Pipeline completed.")


if __name__ == "__main__":
    main()
