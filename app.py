from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("index")
    return render_template('index.html')

@app.route('/snake')
def snake():
    print("snake")
    return render_template('snake.html')

if __name__ == '__main__':
    print("main")
    app.run(debug=True) 