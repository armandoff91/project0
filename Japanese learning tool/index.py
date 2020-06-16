from flask import Flask
from flask import render_template, request
# import the function
from dict import translate2
# import the dictionary
from dict import hira
app = Flask(__name__)
notes = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/lookup', methods=["POST", "GET"])
def lookup():
    input = request.form.get('input')
    try:
        output = translate2(input, hira)
        notes.append(output)
    except:
        output = 'please enter'
    return render_template("look_up.html", output=output, notes=notes)

@app.route('/signup', methods=["GET",'POST'])
def signup():
    new_id = request.form.get('new_id')
    new_pw = request.form.get('new_pw')
    confirm_pw = request.form.get('confirm_pw')

    message = ''

    accounts = open('accounts.txt', 'r')


    info_submitted = False
    if new_id and new_pw and confirm_pw:
        info_submitted = True

    acc_created = False

    acc = {}
    if info_submitted:
        if confirm_pw == new_pw:
            acc.update({str(new_id) : str(new_pw)})
            message = 'account created!'
            accounts = open('accounts.txt', 'w')
            accounts.write(str(acc))
            accounts.close()
        elif confirm_pw != new_pw:
            message = 'passwords do not match, please try again.'
    return render_template('signup.html', info_submitted=info_submitted, message=message)

