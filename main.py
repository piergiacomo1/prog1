from flask import Flask, request, render_template_string

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        vals = request.form.getlist('numero')
        val1 = float(vals[0])
        val2 = float(vals[1])
        result = val1 + val2
    else:
        val1 = ''
        val2 = ''
        result = ''

    return render_template_string('''
    <head>
        <title>Somma</title>
    </head>
    <body>
<h1>Somma di due elementi</h1>
<form action="/" method="POST">
<p>Numero 1: <input type="number" name="numero" value="{{ val1 }}"></p>
<p>Numero 2: <input type="number" name="numero" value="{{ val2 }}"></p>
<input type="submit" value="Somma">
<p>Somma: <input type="number" name="result_dc" value="{{ result }}"></p>
</form>
</body>
''', val1=val1, val2=val2, result=result)

app.run()