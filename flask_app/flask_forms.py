from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from find_degrees import find_degrees
from db import entries

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        start = request.form.get('first_element')
        end = request.form.get('second_element')
        path = find_degrees(start, end, entries)
        print(start)
        print(end)
        print(path)
        if path:
            arrowed_path = ' -> '.join(path)
        else:
            arrowed_path = f'There is no connection between {start} and {end}'
        return render_template('result.html', path=path, arrowed_path=arrowed_path, start=start, end=end)
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, port=-1)
