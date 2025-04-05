from flask import Flask, render_template, url_for

app = Flask(__name__)

PAGES_PATH = 'pages'
pages = [
    {"endpoint": "index", "url": "/", "template": f"{PAGES_PATH}/index.html", "title": "Home"},
    {"endpoint": "resume", "url": "/resume", "template": f"{PAGES_PATH}/resume.html", "title": "Resume"},
    {"endpoint": "portfolio", "url": "/portfolio", "template": f"{PAGES_PATH}/portfolio.html", "title": "Portfolio"},
    {"endpoint": "contact", "url": "/contact", "template": f"{PAGES_PATH}/contact.html", "title": "Contact"},
]

for page in pages:
    def make_view(template, title):
        def view():
            return render_template(template, page=title)
        return view

    app.add_url_rule(
        rule=page["url"],
        endpoint=page["endpoint"],
        view_func=make_view(page["template"], page["title"]),
        methods=["GET"]
    )

if __name__ == "__main_":
    app.run()
