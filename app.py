from flask import Flask, render_template, request

app = Flask(__name__)

# All conversion logic lives here
def convert(value, unit_from, unit_to):

    # --- LENGTH ---
    if unit_from == "km" and unit_to == "miles":
        return round(value * 0.621371, 4)
    elif unit_from == "miles" and unit_to == "km":
        return round(value * 1.60934, 4)

    # --- TEMPERATURE ---
    elif unit_from == "celsius" and unit_to == "fahrenheit":
        return round((value * 9/5) + 32, 4)
    elif unit_from == "fahrenheit" and unit_to == "celsius":
        return round((value - 32) * 5/9, 4)

    # --- WEIGHT ---
    elif unit_from == "kg" and unit_to == "lbs":
        return round(value * 2.20462, 4)
    elif unit_from == "lbs" and unit_to == "kg":
        return round(value * 0.453592, 4)

    # Same unit selected
    elif unit_from == unit_to:
        return value

    else:
        return "Invalid conversion"


# Route: loads the homepage
@app.route("/")
def index():
    return render_template("index.html", result=None)


# Route: handles the form submission
@app.route("/convert", methods=["POST"])
def handle_convert():
    value     = float(request.form["value"])      # the number user typed
    unit_from = request.form["unit_from"]          # e.g. "km"
    unit_to   = request.form["unit_to"]            # e.g. "miles"

    result = convert(value, unit_from, unit_to)

    return render_template("index.html", result=result,
                           value=value, unit_from=unit_from, unit_to=unit_to)


if __name__ == "__main__":
    app.run(debug=True)