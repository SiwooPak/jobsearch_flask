from flask import Flask, render_template, request as req, redirect
import job_scrap

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/search')
def search():
    keyword = req.args.get('keyword')
    if keyword:
        keyword = keyword.lower()
        result = job_scrap.scrap(keyword)
        return render_template("report.html", keyword=keyword, result=result)
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run()  # Flask
