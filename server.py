from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html', page='Home')

@app.route('/resume')
def resume():
    return render_template('pages/resume.html', page='Resume')

@app.route('/portofolio')
def portofolio():
    return render_template('pages/portofolio.html', page='Portofolio')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html', page='Contact')

if __name__ == "__main_":
    app.run()
