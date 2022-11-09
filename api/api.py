from flask import Flask

app = Flask("transp_api")


def response(status, message, http_code):
    return {"status": status, "message": message}, http_code


@app.route("/analyze-portal", methods=["GET"])
def post():
    try:
        return response(True, "ok", 200)
    except:
        return response(False, "error", 500)


app.run()
