import requests
from bs4 import BeautifulSoup
import json

def fetch_url_content(url):
    for _ in range(3):  # Retry up to 3 times
        try:
            response = requests.get(url, timeout=20)  # Increase timeout
            response.raise_for_status()
            return response.text
        except requests.exceptions.Timeout:
            print(f"Timeout occurred for {url}, retrying...")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return None
    return None

def parse_content(url):
    html_content = fetch_url_content(url)
    if not html_content:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')

    if "investopedia" in url:
        overview = soup.find('p').get_text(strip=True) if soup.find('p') else "Overview not available"
        summary = "Mutual Funds Overview from Investopedia"
        description_tag = soup.find('section', {'id': 'mntl-sc-block_1-0'})
        description = description_tag.get_text(strip=True) if description_tag else "Description not available"
        keywords = "Investopedia, Mutual Funds"

    elif "amfiindia" in url:
        overview = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Overview not available"
        summary = "Understanding Mutual Funds from AMFI India"
        description = ''.join([p.get_text(strip=True) for p in soup.find_all('p')[:5]]) or "Description not available"
        keywords = "AMFI, Mutual Funds"

    elif "zerodha" in url:
        overview_tag = soup.find('h1', {'class': 'post-title'})
        overview = overview_tag.get_text(strip=True) if overview_tag else "Overview not available"
        summary = "Introduction to Mutual Funds from Zerodha"
        description = ''.join([p.get_text(strip=True) for p in soup.find_all('p')[:5]]) or "Description not available"
        keywords = "Zerodha, Mutual Funds"

    elif "wikipedia" in url:
        overview = soup.find('p').get_text(strip=True) if soup.find('p') else "Overview not available"
        summary = "Wikipedia Article on Mutual Funds"
        description = ''.join([p.get_text(strip=True) for p in soup.find_all('p')[:5]]) or "Description not available"
        keywords = "Wikipedia, Mutual Funds"

    else:
        print(f"Unsupported URL format: {url}")
        return None

    return {
        "Overview": overview,
        "Summary": summary,
        "Description": description,
        "Keywords": keywords,
        "Link": url
    }

def main():
    urls = [
        "https://www.investopedia.com/terms/m/mutualfund.asp",
        "https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html",
        "https://zerodha.com/varsity/chapter/introduction-to-mutual-funds/",
        "https://en.wikipedia.org/wiki/Mutual_fund"
    ]

    data = []

    for url in urls:
        content = parse_content(url)
        if content:
            data.append(content)

    # Save to JSON file
    with open('mutual_funds_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Data successfully saved to mutual_funds_data.json")

if __name__ == "__main__":
    main()
