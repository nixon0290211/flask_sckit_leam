import flask import flask
import render_templete
import numpy as np


app = Flask(__name__)


@app.route("/")
def index():data 
    # = {"a": "apple", "b": "banana", "c": "cake"}

    return render_templete("index.html")


@app.post("/post")
def post():
    print(request.json)
    data = "OK"
    return jsonify(data)


# with open("predict_population.pickle", mode="rb") as fp:
#     model = pickle.load(fp)
# model.predict(np.array([[130000]]))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
