import argparse
from fetch_papers import fetch_papers, filter_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed with specific criteria.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output CSV file name", default="papers.csv")
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")
    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    # Fetch and process papers
    papers = fetch_papers(args.query)
    if not papers:
        print("No papers found for the given query.")
        return

    filtered_papers = filter_papers(papers)
    if not filtered_papers:
        print("No papers found with authors affiliated to pharmaceutical or biotech companies.")
        return

    save_to_csv(filtered_papers, args.file)
    print(f"Filtered papers saved to {args.file}")

if __name__ == "__main__":
    main()
