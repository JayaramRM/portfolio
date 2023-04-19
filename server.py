from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_page():
    return render_template('index.html')
 
@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

def writefile(data):
    with open('D:/web/dbase.txt', newline='' ,mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def writecsv(data):
    with open('D:/web/database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/formsubmit', methods=['POST', 'GET'])
def formsubmit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writecsv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, try again later'