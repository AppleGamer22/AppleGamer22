from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def main():
    result = ""
    if "q" in request.args:
        try:
            result = eval(request.args["q"])
        except:
            result = "Server Error."
    return """
    <h1 style="text-align:center"> Welcome to my epic claculator </h1><br><br><br>

    <form action="/" style="text-align:center">
        <input type="text" name="q">
        <input type="submit">
    </form>
    <h2 style="text-align:center"> {} </h2>
    """.format(result)

if __name__ == "__main__":
    app.run(port=8002, host='0.0.0.0')