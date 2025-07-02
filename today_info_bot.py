import requests
from datetime import datetime

def get_today_history(month=None, day=None):
    if month is None or day is None:
        today = datetime.now()
        month = today.month
        day = today.day

    url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        events = data["events"]
        print(f"\n📅 Historical Events on {month}/{day}:\n")
        for event in events[:10]:  # Show top 10
            year = event['year']
            description = event['text']
            print(f"• {year}: {description}")
    else:
        print("❌ Failed to fetch data from Wikipedia.")

# 🔹 Ask user for date input
user_input = input("Enter a date (MM/DD) or press Enter to use today: ").strip()

if user_input:
    try:
        month, day = map(int, user_input.split("/"))
        get_today_history(month, day)
    except ValueError:
        print("❌ Invalid date format. Use MM/DD (e.g., 06/30).")
else:
    get_today_history()
