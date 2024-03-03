# TEMA 6: PYTHON EM OUTROS PARADIGMAS

# Módulo 3: Desenvolvimento Web com Python

# Abra o terminal na pasta do seu projeto
# Crie um ambiente virtual usando o comando: python -m venv venv
# Ative o ambiente virtual. No Windows, use o comando: source venv/bin/activate
# Instalar o pacote "flask": pip install Flask
# Crie o arquivo .gitignore e coloque as pastas necessárias

from flask import Flask, request, render_template
 
app = Flask(__name__)
app.debug = True
 
@app.route('/')
def index():
    nome = request.args.get('nome', 'Mundo!')  # Pega o parâmetro 'nome' da URL(http://127.0.0.1:5000/?nome=Marcela), se não houver, usa 'Mundo' como padrão
    return render_template('indice.html', nome_recebido=nome)

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return "Olá, " + nome + "!"

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."
 
if __name__ == '__main__':
    app.run()   # http://127.0.0.1:5000/