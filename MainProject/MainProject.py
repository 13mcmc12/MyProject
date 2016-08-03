from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def load_contacts_from_file():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
