from flask import Flask, render_template, request
from forms import Text
from function import is_palindrome
import string
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = Text()
    result_val = None
    if form.validate() and request.method == 'POST':
        input_val = form.text_field.data
        result_val = is_palindrome(input_val)
    return render_template('index.html', form=form, result = result_val)

if __name__ == '__main__':
    app.run(debug=True)