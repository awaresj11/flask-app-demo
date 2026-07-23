from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")


@app.route("/api/status")
def api_status():
  return jsonify(
    {
      "status": "success",
      "message": "Server is up & running"
    })

@app.route("/health")
def health():
  return (
    jsonify(
        {
           "status": "UP"                                                                           }),
    200 ,)
if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=True)

