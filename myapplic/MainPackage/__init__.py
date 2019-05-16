import os

from flask import Flask, request, json
from selene import config
from selene.browsers import BrowserName

from CustomAddons.behave_methods import do_behave
from myapplic.Tests.pzzBy import pzzBy

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        a = request.get_json()
        do_behave.create_feature(json.dumps(a))
    except AttributeError as ex:
        return 'Error: ' + str(ex)
    return do_behave.run_feature()





if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
