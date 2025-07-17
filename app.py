from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("index")
    return render_template('index.html')

if __name__ == '__main__':
    print("main")
    app.run(debug=True) 