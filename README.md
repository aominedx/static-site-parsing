# Simple Parser

A simple web scraper that extracts product data (name, price, description, image URL) from the Samsung Galaxy category on killprice24.ru and saves it to an Excel file.

## Features

- Extracts product name, price, description, and image link
- Handles pagination automatically
- Saves data to `.xlsx` format
- Realistic browser headers to avoid blocking
- Random delays between requests (1–3 seconds)

##  Technologies

- Python 3.10+
- Requests
- BeautifulSoup4 (lxml parser)
- XlsxWriter

## Result
<img width="893" height="186" alt="image" src="https://github.com/user-attachments/assets/4095bb59-d338-4df6-a88c-721c8bd79f33" />


##  Installation

```bash
git clone https://github.com/your-username/killprice-parser.git
cd killprice-parser
pip install -r requirements.txt

