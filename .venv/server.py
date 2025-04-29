from tkinter import image_names

from flask import Flask, render_template
# from markupsafe import escape
import sys
import pathlib

app = Flask(__name__)
print(app)
@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)
#
# @app.route('/index.html')
# def index():
#     return render_template('./index.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('./works.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, Debug=True)