import re
import json


with open("c:/Users/archa/Desktop/pptwo/Week5/Practice5/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract all prices from the receipt
price_pattern = r"Стоимость\n([\d ]+,\d{2})"
prices = re.findall(price_pattern, text)

clean_prices = []
for p in prices:
    number = p.replace(" ", "").replace(",", ".")
    clean_prices.append(float(number))
    
# Find all product names
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)

# Calculate total amount
total = sum(clean_prices)

# Extract date and time information
date_pattern = r"\d{2}\.\d{2}\.\d{4}"
time_pattern = r"\d{2}:\d{2}:\d{2}"

date = re.search(date_pattern, text)
time = re.search(time_pattern, text)

# Extract date and time information
payment_pattern = r"Банковская карта"
payment = re.search(payment_pattern, text)

# Create a structured output (JSON or formatted text)
receipt_data = {
    "products": products,
    "prices": clean_prices,
    "calculated_total": total,
    "date": date.group() if date else None,
    "time": time.group() if time else None,
    "payment_method": payment.group() if payment else None
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))