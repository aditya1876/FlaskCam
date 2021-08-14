'''
This version includes :
    * Changes till version2
    * 

'''

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def resultchecker():
    avg_score = 0
    if request.method == 'POST':
        marks_sci = float(request.form['science_n'])
        marks_mat = float(request.form['maths_n'])
        marks_c = float(request.form['c_n'])
        marks_ds = float(request.form['datascience_n'])
        avg_score = (marks_sci+marks_mat+marks_c+marks_ds)/4

    return redirect(url_for('final_result', score=int(avg_score)))


@app.route('/result/<int:score>')
def final_result(score):
    res = ''
    if score < 50:
        res = 'FAILED'
    else:
        res = 'PASSED'

    return render_template('result2.html', result=res, marks=score)


if __name__ == '__main__':
    app.run(debug=True)
