import os
from flask import Flask, request, redirect, url_for, send_from_directory, flash, render_template
from werkzeug.utils import secure_filename
from datetime import date
from create_html import *


UPLOAD_FOLDER = '/home/ben/programming/volta/uploads/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__, template_folder='/home/ben/programming/volta/templates/created_pages/', static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            today = date.today()
            filename = str(today.month) + "-" + str(today.day) + "-" + str(today.year) + ".csv"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # creates a html file from the csv file
            create_dict(filename)
            return redirect(url_for('report', date=filename.split(".")[0]))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/report/<date>')
def report(date):
    return render_template(date + ".html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.secret_key = "my_secret"
    app.run(debug=True)
