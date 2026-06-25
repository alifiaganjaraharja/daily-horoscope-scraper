# 🔮 Scrape Horoscope Website Toolkit

This repository includes all of the information, such as a CSV result file, the Python script (scraper.py), and a workflow to automate the process every day for a year starting from June 11, 2026.
The URL scraped here is [horoscrope.com](https://www.horoscope.com/us/index.aspx) to scrape these 3 informations (Love Match, Friendship Match, and Career Match) around Today's Matches for a specific zodiac sign, which is Taurus for further analysis.
This project is for personal purposes only, and mostly for fun. 

## Usage
```python
from cleaners import remove_duplicates, fill_missing

df = remove_duplicates(df)
df = fill_missing(df, strategy="median")
```

## Setup
```bash
pip install -r requirements.txt
```

Use this code depending on your case

**Notes to Alifia:** Use the Anaconda Navigator -> Jupyter Notebook to clean the dataset.

Alifia G.
