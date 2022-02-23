
import numpy as np
import pickle
from sklearn import linear_model
from app import app
from flask import Flask, request, render_template
from app import estim

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
          vals = request.form.getlist('numero')
          val1 = float(vals[0])
          val2 = float(vals[1])
          val3 = float(vals[2])
          result = estim.estim1(vals)
     else:
          val1 = ''
          val2 = ''
          val3 = ''
          result = ''
     return render_template('''index.html''', val1=val1, val2=val2,val3=val3, result=result)