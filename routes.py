from main import app  

@app.route("/")
def homepage():
    return "Pinterest meu primeiro site no ar!!!!"

@app.route("/perfil")
def perfil():
    return "perfil do usuario"

if __name__=="__main__":
    app.run(debug=True)