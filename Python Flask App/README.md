# Currency Converter in Python (Flask + API)

This project is a simple **Currency Converter Web App** built with Python and Flask.  
It uses the **ExchangeRate API** to fetch real-time exchange rates and converts between different currencies.  
You can run it on your localhost and access it in your browser.

---

## Features
- Convert between multiple currencies (USD, PKR, SAR, EUR, INR, etc.).
- Fetches **live exchange rates** from the internet.
- Simple **web form interface** built with Flask and HTML.
- Handles invalid currency codes gracefully.

---

## Installation & Setup

### 1. Clone or Download the Project
Save the project file as `app.py`.

### 2. Install Dependencies
Make sure you have Python 3 installed. Then, in your terminal:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask App
```bash
python app.py
```

### 4. Open in Browser
Go to:
```
http://127.0.0.1:5000/
```

---

## Example Usage
1. Enter `100` as the amount.  
2. Enter `USD` as base currency.  
3. Enter `SAR` as target currency.  

Output:
```
100 USD = 375.00 SAR
```

*(The values depend on live exchange rates.)*

---

## Project Structure
```
currency-converter/
│
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

---

## Future Enhancements
- Add a dropdown list of supported currencies instead of typing codes.
- Create a better frontend with Bootstrap or Tailwind.
- Add error handling for network failures.
- Save previous conversions in a history log.

---

