from flask import Flask, request

run()
app = Flask(__name__)

@app.route("/")
def main():
    result = ""
    if "q" in request.args:
        result = request.args["q"]
    isInputSafe = True
    for keyword in ["eval", "exec", "import", "open", "os", "read", "system", "write"]:
        if keyword in result:
            isInputSafe = False
    if isInputSafe:
        try:
            result = eval(result)
        except:
            result = "Server error."
    else:
        result = "Invalid input."

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