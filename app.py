from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Currency Converter</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Currency Converter</h2>
    <form method="post">
        Amount: <input type="text" name="amount"><br><br>
        From Currency : <input type="text" name="from_currency"><br><br>
        To Currency : <input type="text" name="to_currency"><br><br>
        <button type="submit">Convert</button>
    </form>
    {% if result %}
        <h3>{{ result }}</h3>
    {% endif %}
</body>
</html>
"""

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()
    
    if to_currency.upper() not in data["rates"]:
        return f"Currency '{to_currency}' not available."
    
    rate = data["rates"][to_currency.upper()]
    converted = amount * rate
    return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        result = convert_currency(amount, from_currency, to_currency)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
