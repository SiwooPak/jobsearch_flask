from flask import Flask, render_template, request as req, redirect, send_file
import job_scrap
from toCsv import save_to_file as save

app = Flask(__name__)

db = {}


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/search')
def search():
    keyword = req.args.get('keyword')
    # 검색 단어가 있다면
    if keyword:
        # 글자를 소문자로
        keyword = keyword.lower()
        # db 변수에 해당검색어가 값 할당
        from_db = db.get(keyword)
        # 해당 키워드에 검색결과가 있다면 result 변수에 할당
        if from_db:
            result = from_db
        # 없다면 해당 검색어를 스크래핑해서 result 변수에 할당
        # db변수에 해당키워드의 키로 결과를 저장
        else:
            result = job_scrap.scrap(keyword)
            count = len(result)
            db[keyword] = result
    # 검석어가 없다면 리다이렉트
    else:
        return redirect("/")
    return render_template("report.html", keyword=keyword, jobs=result, count=count)


@app.route("/download")
def download_csv():
    try:
        keyword = req.args.get("keyword")
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        print(f"Generate CSV for {keyword}")
        save(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


if __name__ == "__main__":
    app.run()  # Flask
