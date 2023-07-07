from flask import Flask, request
app=Flask(__name__)

@app.route("/members",methods=["GET"])
def members():
    return {"message": "working"}

@app.route('/user-data', methods=["POST"])
def handle_user_data():
    data = request.get_json()
    if(data):
        print(data)
    return {"message": "working"} ,200



if __name__== "__main__":
    app.run(debug=True)