from flask import Flask, render_template, flash, redirect, url_for
import datetime
from flask import request
import smtplib
import os

app = Flask(__name__)
year = datetime.datetime.now().strftime("%Y")

PAGES_PATH = 'pages'
pages = [
    {"endpoint": "index", "url": "/", "template": f"{PAGES_PATH}/index.html", "title": "Home"},
    {"endpoint": "resume", "url": "/resume", "template": f"{PAGES_PATH}/resume.html", "title": "Resume"},
    {"endpoint": "portfolio", "url": "/portfolio", "template": f"{PAGES_PATH}/portfolio.html", "title": "Portfolio"},
    {"endpoint": "contact", "url": "/contact", "template": f"{PAGES_PATH}/contact.html", "title": "Contact"},
]


def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with smtplib.SMTP(host=os.environ["MY_HOST"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Message from my website\n\nFrom: {name}, email: {email}\n\nMessage:\n\"{message}\""
        )

for page in pages:
    def make_view(template, title):
        def view():
            if title == "Contact" and request.method == "POST":
                send_email()
            return render_template(template, page=title, year=year)
        return view

    app.add_url_rule(
        rule=page["url"],
        endpoint=page["endpoint"],
        view_func=make_view(page["template"], page["title"]),
        methods=["GET", "POST"]
    )


if __name__ == "__main_":
    app.run()

