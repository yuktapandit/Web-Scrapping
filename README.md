# Mutual Funds Information Scraper

This repository contains a Python script for scraping information about mutual funds from selected websites and saving it in a structured JSON format. The tool is designed to extract data programmatically from trusted financial sources.

## Features
- Fetches data from the following URLs:
  - [Investopedia](https://www.investopedia.com/terms/m/mutualfund.asp)
  - [AMFI India](https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html)
  - [Zerodha Varsity](https://zerodha.com/varsity/chapter/introduction-to-mutual-funds/)
  - [Wikipedia](https://en.wikipedia.org/wiki/Mutual_fund)
- Extracts specific fields: Overview, Summary, Description, Keywords, and the Link.
- Handles HTTP request errors and retries up to 3 times for failed connections.
- Saves the data in a JSON file (`mutual_funds_data.json`).

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```
2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python scrape_mutual_funds.py
    ```
2. Upon successful execution, the script generates a file named `mutual_funds_data.json` in the current directory, containing the extracted data.


## Error Handling
- Retries up to 3 times for failed connections due to timeouts.
- Gracefully handles missing HTML elements by providing default messages like "Overview not available" or "Description not available."

## Dependencies
- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies with:
```bash
pip install requests beautifulsoup4
```
