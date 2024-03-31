from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/check_teeth_health', methods=['POST', 'GET'])
def result():
    return render_template("result.html")

@app.route('/do_stuff', methods=['POST', 'GET']) 
def check_teeth_health():
    if request.method == 'POST':
        mineralization = request.form['mineralization']
        calcification = request.form['calcification']
        cavities = request.form['cavities']
        bacteria_content = request.form['bacteria_content']
        tooth_density = request.form['tooth_density']

        conditions_met = 0  # Counter for conditions met

        if int(mineralization) < 80:
            message = 'Mineralization is low, cavity warning.'
            conditions_met += 1

        if int(calcification) > 30:
            message = 'High cavity risk, plaque presence is high.'
            conditions_met += 1

        if int(bacteria_content) > 10e+5:
            message = 'You are exhibiting gum disease risk factors.'
            conditions_met += 1

        if int(cavities) >= 1:
            message = 'You have at least one cavity.'
            conditions_met += 1

        if float(tooth_density) < 2.84 or float(tooth_density) > 3:
            message = 'Your enamel has experienced erosion.'
            conditions_met += 1

        if conditions_met > 4:
            result = 'See a physician as soon as possible.'
        elif conditions_met > 3:
            result = 'Urgent dental care needed.'
        elif conditions_met > 2:
            result = 'You are exhibiting risk factors for multiple oral conditions. Take preventative measures as soon as possible.'
        elif conditions_met >= 1:
            result = 'Your oral health could be at risk.'
        else:
            result = 'Your teeth are healthy!'

        return HELLO_HTML.format(result)
        

HELLO_HTML = """

<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Menu</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link href="{{ url_for('static', filename='css/style2.css') }}" rel="stylesheet">
</head>
     
<body>
<div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper" style="width: 250px;">
        <div class="sidebar-heading"></div>
        <div class="list-group list-group-flush">
            <a href="http://localhost:5000/" class="list-group-item list-group-item-action bg-light">Home</a>
            <a href="http://localhost:5000/page2" class="list-group-item list-group-item-action bg-light">Profile</a>
            <a href="http://localhost:5000/check_teeth_health" class="list-group-item list-group-item-action bg-light">Dental Health Status</a>
        </div>
    </div>

    <!-- Page Content -->
    <div id="page-content-wrapper" style="flex: 1;">

        <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
            <button class="btn btn-primary" id="menu-toggle">Toggle Menu</button>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="http://localhost:5000/page3">Login</a>
                    </li> 
                </ul>
            </div>
        </nav>

        <div class="container-fluid">
            <div class="card mt-4">
                <div class="card-body">
                    <h2 class="card-title">Diagnosis: {0}</h2>
                </div>
            </div>
        </div>
    </div>

</div>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

</body>
</html>

     
     """


if __name__ == '__main__':
    app.run()

