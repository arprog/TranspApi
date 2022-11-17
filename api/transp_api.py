from flask import Flask, jsonify, request
from scraping.script_executor.script_executor import run_scrapy_shell_script

app = Flask(__name__)


def response(status, message, http_code):
    return {"status": status, "message": message}, http_code


@app.route("/analyze-portal", methods=["POST"])
def analyze_portal():
    request_ = request.json
    run_scrapy_shell_script("transparencies")

    return jsonify()


app.run()
