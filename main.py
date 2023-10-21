from flask import Flask, request, render_template, redirect
from app import get_uploadedpic_color, get_simular_sock

app = Flask(__name__)


def answes(path):
    responses = {'path': path}
    return responses


@app.route('/')
def index():
    return render_template('index.html')


'''@app.route('/results', methods=['GET', 'POST'])
def getResults():
    if request.method == 'POST':
        return redirect('/results')

    userinp = request.form.get('userinp')
    return render_template('results.html', image=userinp)'''


@app.route('/results', methods=['GET', 'POST'])
def getResults():
    if request.method == 'POST':
        userinp = request.files['userinp']
        userinp.save('static/uploaded_image.jpg')  # Save the uploaded file

        # Call your function with the saved file path
        image = get_simular_sock('static/uploaded_image.jpg')
        sockPath = image
        print(sockPath)
        return render_template('results.html', sockPath=sockPath, image=image)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
