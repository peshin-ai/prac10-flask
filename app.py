from flask import Flask

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/Tuan')
def greet(name="Ung Ta Hoang Tuan"):
    return "Hello {}".format(name)


if __name__ == '__main__':
    app.run()
