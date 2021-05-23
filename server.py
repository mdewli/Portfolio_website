from flask import Flask
from flask import render_template, url_for, request, redirect
from flask.wrappers import Request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = f.write(f"\n {email},{subject},{message}")
        
def write_to_csv(data):
    with open('database.csv',newline="", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvwriter = csv.writer(database, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou_page.html")
        except:
            return 'Could not save your message to Database. Please try again.'
    else:
        return "something went wrong! Please try again"



if __name__=="__main__":
    app.run(debug=False)