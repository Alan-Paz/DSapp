
# A very simple Flask Hello World app for you to get started with...

#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("sistema.html")


       # @app.route("/", methods=["GET", "POST"])
#def index():
    #if request.method == 'GET':
       # return render_template("selecoes.html")

     #   from flask import Flask, request, render_template
######'password': 'sua_senha',
    #'database': 'seu_banco_de_dados'
#}

#3@app.route('/login', methods=['POST', 'GET'])
#def login():
 #   if request.method == 'POST':
  #      username = request.form['username']
   #     password = request.form['password']

        # Conexão com o banco de dados
    #    try:
     #       conn = mysql.connector.connect(**db_config)
      #      cursor = conn.cursor()

       #     query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        #    cursor.execute(query, (username, password))
         #   user = cursor.fetchone()

          #  if user:
           #     return "Login bem-sucedido!"
            #else:
             #   return "Usuário ou senha incorretos."

        #except mysql.connector.Error as err:
         #   return f"Erro ao conectar-se ao banco de dados: {err}"
        #finally:
         #   cursor.close()
          #  conn.close()

    #return render_template('login.html')

#if __name__ == '__main__':
 #   app.run()


