'''
Version1 covers
- basic routing
- Dynamic URL generation
- reditect and url_for
'''
from flask import Flask, redirect, url_for

app = Flask(__name__)

# Page routing


@app.route("/")
def welcome():
    return "Access webcam using Flask."


# Dynamically generated URL
@app.route("/pass/<int:score>")  # url will show integer varaible score
def passPage(score):  # fn will take the score coming from the URL
    return "You are redirected here because you have passed with a score of " + str(score)


@app.route("/fail/<int:score>")  # url will show integer varaible score
def failPage(score):  # fn will take the score coming from the URL
    return "You are redirected here because you havblacke failed with a score of " + str(score)


# Page redirection and url_for
@app.route("/results/<int:marks>")  # url will show integer varaible score
def evaluate(marks):  # fn will take the score coming from the URL
    result = ""
    if marks > 50:
        result = "passPage"
    else:
        result = "failPage"

    return redirect(url_for(result, score=marks))
    # 'results' variable tell which funcction to call to take and 'score' is the variable taken by the functions and we need to provide the value to be passed to it.


if __name__ == "__main__":
    app.run(debug=True)
