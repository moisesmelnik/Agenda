# Rota principal que redireciona para login se o usuário não estiver autenticado

# Importação de bibliotecas principais do Flask para web, sessão e templates
from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime, date
# Importação do cliente Firestore da Google Cloud para acessar o banco NoSQL
from google.cloud import firestore
import os

# Define a variável de ambiente com o caminho para as credenciais do Firestore
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__), "agenda1-464719-5a0b388ebd41.json")

# Cria uma instância do aplicativo Flask
app = Flask(__name__)
# Chave secreta para proteger sessões e cookies (deveria ser armazenada com segurança em produção)
app.secret_key = 'supersecretkey'
# Inicializa o cliente Firestore autenticado
db = firestore.Client()

# Função que calcula idade a partir da data de nascimento e verifica se hoje é aniversário
def calcular_idade(data_nascimento):
    hoje = date.today()
    try:
        nasc = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    except ValueError:
        return None, False
    idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
    aniversario_hoje = (hoje.day == nasc.day and hoje.month == nasc.month)
    return idade, aniversario_hoje

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    return redirect('/cadastrar')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user_ref = db.collection('usuarios').document(username)
            user_doc = user_ref.get()
            if user_doc.exists and user_doc.to_dict().get('senha') == password:
# Armazena o nome de usuário na sessão para autenticação futura
                session['username'] = username
                return redirect(url_for('cadastrar'))
            else:
                return 'Usuário ou senha inválidos'
        except Exception as e:
            return f'Erro ao acessar o banco de dados: {str(e)}'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if 'username' not in session:
        return redirect('/login')

    resultado = []
    dados_formulario = {}

    if request.method == 'POST':
        doc_id = request.form.get('documento_id')

        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        fiscal = request.form.get('fiscal')
        fisco_id = request.form.get('fisco_id')
        data_nascimento = request.form.get('data_nascimento')
        idade, aniversario_hoje = calcular_idade(data_nascimento)
        cep = request.form.get('cep')
        rua = request.form.get('rua')
        numero = request.form.get('numero')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        pais = request.form.get('pais')
        telefones = request.form.getlist('telefones')
        email = request.form.get('email')
        facebook = request.form.get('facebook')
        instagram = request.form.get('instagram')
        notas = request.form.get('notas')

        if not idade:
            return "Data de nascimento inválida", 400
        
# Cria o dicionário com todos os dados coletados do formulário para salvar no Firestore
        pessoa = {
            'nome': nome,
            'sobrenome': sobrenome,
            'fiscal': fiscal,
            'fisco_id': fisco_id,
            'data_nascimento': data_nascimento,
            'idade': idade,
            'aniversario_hoje': aniversario_hoje,
            'cep': cep,
            'rua': rua,
            'numero': numero,
            'bairro': bairro,
            'municipio': municipio,
            'estado': estado,
            'pais': pais,
            'telefones': telefones,
            'email': email,
            'facebook': facebook,
            'instagram': instagram,
            'notas': notas,
            'timestamp': datetime.now()
        }

        if doc_id:
            db.collection('familia').document(doc_id).set(pessoa)
        else:
            db.collection('familia').add(pessoa)
        return redirect('/cadastrar')

    elif request.method == 'GET':
        nome = request.args.get('nome')
# Se 'documento_id' está presente, atualiza o documento existente. Caso contrário, cria um novo.
        fisco_id = request.args.get('fisco_id')

        if nome or fisco_id:
            consulta = db.collection('familia')
            if nome:
                consulta = consulta.where('nome', '==', nome)
            elif fisco_id:
                consulta = consulta.where('fisco_id', '==', fisco_id)
            docs = consulta.stream()
            for doc in docs:
                dados = doc.to_dict()
                dados['documento_id'] = doc.id
                resultado.append(dados)
            if resultado:
                dados_formulario = resultado[0]

    return render_template('cadastro.html', resultado=resultado, dados=dados_formulario)

@app.route('/deletar/<documento_id>', methods=['POST'])
def deletar(documento_id):
    if 'username' not in session:
        return redirect('/login')
    db.collection('familia').document(documento_id).delete()
    return redirect('/cadastrar')

if __name__ == '__main__':
    app.run(debug=True)
