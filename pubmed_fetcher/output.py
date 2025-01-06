import pandas as pd

def save_results_to_csv(results, filename="papers.csv"):
    """Save parsed results to a CSV file."""
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")