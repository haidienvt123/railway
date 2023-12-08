from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        print(file)
        if file is None or file.name == "":
            return jsonify(error = "no file")
        
        try:
            raw_data = file.read().decode("utf-8") 
            return_data = jsonify(data = raw_data)
            return return_data
            # return {"status":"not bug"}
        except Exception as e:
            return jsonify(error = str(e))
            # return {"status":"bug"}
        
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))