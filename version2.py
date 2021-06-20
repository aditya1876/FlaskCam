'''
Version 2 covers
- render html templates
- jinja2 templating
'''

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

'''
Rendering html pages in jinja2 templating engine requires a folder structure as follows:
project > templates > (html files)
'''

# rendering a template


@app.route("/")
def welcome():
    return render_template('index.html')

# reading from forms and rendering to a html page


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    avgtotalmarks = 0
    if request.method == 'POST':
        science_marks = float(request.form['science_n'])
        maths_marks = float(request.form['maths_n'])
        c_marks = float(request.form['c_n'])
        datascience_marks = float(request.form['datascience_n'])
        avgtotalmarks = (science_marks+maths_marks+c_marks+datascience_marks)/4

    result = ""
    if avgtotalmarks >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    return render_template('result.html', final_res=result)
    # 'final_result' should be in the result.html as varialble so that it can show the value of 'result' variable from here.


if __name__ == "__main__":
    app.run(debug=True)
