import mypythonmodule
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle the form submission
@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        number = request.form['number']
        result = mypythonmodule.get_cpp_string(number)
        print(result)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
