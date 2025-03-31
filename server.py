from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('template.html', page='Home')

@app.route("/portofolio")
def portofolio():
    return render_template('template.html', page='Portofolio')

@app.route("/resume")
def resume():
    return render_template('template.html', page='Resume')

@app.route("/contact")
def contact():
    return render_template('template.html', page='Contact')

if __name__ == "__main_":
    app.run()
