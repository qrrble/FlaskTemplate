from flaskexample import app
from flask import render_template
from flask import request
from functions import *

@app.route('/')
def index():


    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    integer_input = request.form['integer_input']

    # Checks to see if the input is an integer.
    # If not, then return an error message.
    try:
        float_value = float(integer_input)
        if not float_value.is_integer():
            return "ERROR: Input not an integer!"
    except:
        return "ERROR: Input not an integer!"


    integer_input = int(integer_input)
    # Generates a plot 
    output_plot = PlottingFunction(integer_input)

    return render_template("result.html", output_plot = output_plot)