"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
from app import app
from flask import render_template, request, jsonify, send_file,flash,redirect
import os
from app.forms import UploadForm


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/upload',methods=['POST'])
def upload():
    uploadForm = UploadForm()

    if uploadForm.validate():
        description = uploadForm.description.data
        photo = uploadForm.photo.data
        if photo.filename == '':
                flash('No selected Photo')
                print("No selected Photo")
                return redirect(request.url)
        
        photoname = secure_filename(photo.filename)
        photo.save(str(os.path.join(app.config['UPLOADS_FOLDER'],photoname)))

        return {
            'message': "File upload complete",
            'filename': f"{photoname}",
            'description': f"{description}"
        }
    else:
        error_arr =[]
        errors = form_errors(uploadForm)

        #loop over errors, created a JSON for each
        for x in range(len(errors)):
            obj = {f"{x}":errors[x]}
            error_arr.appdend(obj)

        return {
            'errors': error_arr
        }
        
        




    


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")