from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        return redirect('/results')
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)
