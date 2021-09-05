from flask import Flask, render_template
import network
app = Flask(__name__)

@app.route('/')
def index():
    person = network.person
    male = "Male"
    female = "Female"
    if person > 0.5:
        gender = female
    else:
        gender = male
    return render_template("index.html", gender=gender)


if __name__ == "__main__":
    app.run(debug=True)