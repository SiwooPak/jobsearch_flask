from flask import Flask, render_template, request as req

app = Flask("Search my job")


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/search')
def contact():
    keyword = req.args.get('keyword')
    return render_template("report.html", keyword=keyword)


if __name__ == '__main__':
    app.run()
