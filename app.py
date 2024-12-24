from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            result = "Invalid operation"
        return render_template("calculator.html", result=result)
    except Exception as e:
        return render_template("calculator.html", result=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
