from flask import Flask, render_template, request
from unit_converter import convert_units

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
        except ValueError:
            return render_template('index.html', error='Invalid value')
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_units(value, from_unit, to_unit)
        if isinstance(result, str):
            return render_template('index.html', error=result)
        else:
            return render_template('index.html', result=result)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run()
