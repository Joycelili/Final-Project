from flask import Flask, request

app= Flask(__name__)

# necesario en pythonanywhere
#PATH=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home ():
    return "Welcome to my Api"

if __name__=="__main__":
    app.run(debug=False)
