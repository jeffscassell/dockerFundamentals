"""
backend.main
~~~~~~~~~~~~

Here is a docstring for this module.
"""


from flask import Flask



app = Flask("backend route")

@app.route("/")
def main():
    """ Docstring for function. """
    return {"msg": "Hello world"}

@app.route("/string")
def getString():
    """ something """
    return "Hello world"