from main import app  

@app.route("/")
def homepage():
    return "Pinterest meu primeiro site no ar!!!!"

if __name__=="__main__":
    app.run(debug=True)