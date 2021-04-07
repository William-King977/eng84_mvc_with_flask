from flask import Flask, render_template

# Creating an app instance
app = Flask(__name__)

# Use a decorator @ to define the route for our webpage
@app.route("/")

# Setting up a default page
def index():
    return render_template("index.html")

@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

# Create 2 more pages/routes and add the functionality for email and password
# Implement OOP and inheritance
@app.route("/buttons/")
def buttons():
    return render_template("buttons.html")

if __name__ == "__main__":
    app.run(debug=True)











