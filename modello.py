from flask import Flask, request, render_template_string
import numpy as np
from sklearn import linear_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    x = np.array([[ 56755.72171242,  44178.04737774,  40991.80813814],   [8814.00098681, 43585.51198178,  13574.17183072],   [6175.8760297 ,  17829.69832237, 53254.85637009],  [17522.23018625,  42784.69836164,  36638.18492916], [41086.72967373,  18167.77372717,  12706.89121489],  [52564.42917946, 61995.42280258,  35776.79516181],  [30230.22630213,  34524.46986093, 13774.60527391],  [14258.22933451, 101376.49657434,   9616.64500569], [45175.23189338,  38615.99518491,  74355.51585756],  [12578.49547344, 19242.3664711 ,  16310.988409]  ,  [20881.76692993,   5734.63362915, 25732.01836475],  [51545.48360953,  82081.59716162,  11006.2497364]])
    y = np.array([7.3, 6.4, 6.3, 5.7, 7.0, 7.5, 6.0, 5.9,  7.4, 6.1, 5.9, 7.3])
    linmodel = linear_model.LinearRegression(fit_intercept=True)
    linmodel.fit(x, y)

    if request.method == 'POST':
        vals = request.form.getlist('numero')
        val1 = float(vals[0])
        val2=float(vals[1])
        val3 = float(vals[2])
        x1=np.array([[val1,val2,val3]])
        result =float(linmodel.predict(x1))
    else:
        val1 = ''
        val2 = ''
        val3 = ''
        result = ''

    return render_template_string('''
    <head>
        <title>Regressione</title>
    </head>
    <body>
<h1>Regressione lineare</h1>
<form action="/" method="POST">
<p>Numero 1: <input type="number" name="numero" value="{{ val1 }}"></p>
<p>Numero 2: <input type="number" name="numero" value="{{ val2 }}"></p>
<p>Numero 3: <input type="number" name="numero" value="{{ val3 }}"></p>
<input type="submit" value="modella">
<p>valore previsto: <input type="number" name="result_dc" value="{{ result }}"></p>
</form>
</body>
''', val1=val1, val2=val2,val3=val3, result=result)

app.run()