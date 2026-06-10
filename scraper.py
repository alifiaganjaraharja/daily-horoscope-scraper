import requests
from bs4 import BeautifulSoup
import csv
import datetime
import os

url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Fetching today's horoscope data...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    love_sign = "Not found"
    friendship_sign = "Not found"
    career_sign = "Not found"
    
    all_h4s = soup.find_all('h4')
    for h4 in all_h4s:
        text = h4.text.strip().lower()
        if text == 'love':
            love_sign = h4.find_next('p').text.strip()
        elif text == 'friendship':
            friendship_sign = h4.find_next('p').text.strip()
        elif text == 'career':
            career_sign = h4.find_next('p').text.strip()

    # Get today's date formatted as YYYY-MM-DD
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    
    csv_file = "horoscope_matches.csv"
    file_exists = os.path.isfile(csv_file)
    
    # Open the CSV file in append mode ('a')
    with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # If the file doesn't exist yet, write the header row first
        if not file_exists:
            writer.writerow(["Date", "Love Match", "Friendship Match", "Career Match"])
            
        # Append today's data
        writer.writerow([today_date, love_sign, friendship_sign, career_sign])
        
    print(f"Successfully saved today's data to {csv_file}!")

else:
    print(f"Failed to connect. Error code: {response.status_code}")