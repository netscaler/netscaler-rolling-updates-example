from flask import Flask
import sys

app = Flask(__name__)


@app.route("/")
def hello():
    if len(sys.argv) >= 2:
        return "%s\n" % str(sys.argv[1])
    return "Hello World!\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
