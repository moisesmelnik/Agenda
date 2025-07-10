# 📘 Agenda Familiar

**Agenda Familiar** é uma aplicação web desenvolvida com Flask e Firestore para o cadastro, busca, edição e exclusão de registros pessoais com controle de autenticação, busca por CPF/nome, máscaras dinâmicas e preenchimento automático de endereço via API do ViaCEP.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Firestore (Firebase)
- HTML5 + CSS3
- JavaScript (vanilla)
- Jinja2
- API ViaCEP

---

## 🗂️ Estrutura do Projeto

```
Agenda1/
├── app.py                        # Código principal do backend Flask
├── requirements.txt             # Dependências da aplicação
├── start.sh                     # Script para iniciar a aplicação no Render
├── agenda1-*.json               # Credencial do Firebase Firestore
├── static/
│   ├── fundo.webp               # Imagem de fundo da interface
│   ├── style-cadastro.css       # Estilo visual da tela de cadastro
│   ├── style-login.css          # Estilo visual da tela de login
│   └── css/login.css            # Estilo adicional de login
├── templates/
│   ├── cadastro.html            # Tela principal de cadastro e busca
│   ├── familia.html             # Visualização em tabela dos registros
│   ├── index.html               # Página intermediária de rota
│   └── login.html               # Tela de login
```

---

## 📋 Funcionalidades

- ✅ Login com autenticação simples (usuário: `admin`, senha: `1234`)
- 🔍 Busca por nome ou CPF/CNPJ
- 📋 Cadastro completo com endereço, telefone, notas e tipo de pessoa
- ✏️ Edição de dados carregados via busca
- 🗑️ Exclusão de registros
- 🎯 Máscaras dinâmicas para CPF, CNPJ, CEP, datas
- 🌍 Consulta automática de endereço via [API ViaCEP](https://viacep.com.br)

---

## 📦 Instalação Local

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/Agenda1.git
cd Agenda1

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python app.py
```

---

## 🌐 Deploy no Render (opcional)

1. Crie uma conta em [https://render.com](https://render.com)
2. Crie um novo **Web Service**
3. Suba este projeto para um repositório no GitHub
4. Aponte o Render para o repositório
5. Configure:
   - **Runtime**: Python 3
   - **Start Command**: `./start.sh`
   - **Build Command**: `pip install -r requirements.txt`
   - **Environment Variable**:
     - `GOOGLE_APPLICATION_CREDENTIALS=agenda1-xxxx.json`
6. Publique! 🚀

---

## 👨‍💻 Usuário de Teste

```
Usuário: admin
Senha: 1234
```

---

## 🧠 Estrutura Lógica

- `login.html`: autenticação via POST → guarda `username` na sessão
- `cadastro.html`: formulário GET para busca e POST para salvar/editar
- `familia.html`: exibe registros do Firestore em tabela
- `app.py`:
  - Gerencia rotas: `/`, `/login`, `/logout`, `/cadastrar`, `/deletar`
  - Conecta ao Firestore via `google.cloud.firestore`
  - Gera mensagens de alerta e contexto de dados
  - Calcula idade e aniversários

---

## 🛡️ Segurança

> Para produção:
- Nunca exponha a credencial `*.json`
- Utilize variáveis de ambiente seguras
- Implemente autenticação OAuth ou JWT se necessário

---



---

## 🔄 Versão Unificada: Local + Nuvem

Esta versão da aplicação foi estruturada para funcionar **tanto localmente (em seu computador)** quanto **na nuvem (Render.com)** sem a necessidade de manter dois projetos separados.

### ✅ O que foi feito:

- Os arquivos de deploy (`render.yaml`, `start.sh`) foram adicionados ao projeto, mas **não interferem** na execução local.
- A aplicação pode ser iniciada:
  - Localmente via `python app.py` ou `start_app.bat`
  - Na nuvem via Render.com com o uso do `render.yaml`
- Toda a lógica e estrutura de dados permanece centralizada em uma única base de código.

Manter uma versão unificada facilita a manutenção, o versionamento no GitHub e a consistência entre ambientes.

## 📄 Licença

Este projeto é livre para fins de aprendizado e uso pessoal.
Desenvolvido por Moisés D’Anthony Melnik – Eng. da Computação.


---



---

## 📘 Sobre o Projeto

A **Agenda Familiar** é uma aplicação web desenvolvida com Python (Flask) que permite cadastrar, visualizar, buscar e editar informações de pessoas — com foco em facilitar a gestão de contatos familiares, pessoais ou profissionais. O sistema permite ainda buscas por CPF/CNPJ com máscaras automáticas, relação com múltiplos telefones, endereços detalhados e interface adaptada para dispositivos móveis.

---

## 🧱 Estrutura do Projeto

```
Agenda1/
├── app.py                       # Backend em Flask
├── requirements.txt            # Dependências Python
├── start.sh / start_app.bat    # Inicialização Linux/Windows
├── templates/                  # HTMLs (telas)
│   ├── login.html
│   ├── cadastro.html
│   ├── familia.html
├── static/                     # CSS, imagens e estilos
│   ├── fundo.webp
│   └── css/
│       ├── login.css
├── agenda1-XXXX.json           # Chave de autenticação Firestore
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- HTML5 e CSS3
- Google Firebase / Firestore
- Jinja2
- Editor: Visual Studio Code

---

## 🚀 Como Executar Localmente

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Ative o ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Execute a aplicação:

```bash
python app.py
```

Ou clique duas vezes em `start_app.bat` (Windows).

---

## 🔐 Login e Segurança

O sistema exige login:
- **Usuário padrão:** `admin`
- **Senha:** `1234`  
Esses dados estão armazenados de forma simples no Firestore e podem ser modificados diretamente na coleção de autenticação.

---

## 🔍 Funcionalidades Principais

- Cadastro completo com CPF/CNPJ e relação (Cliente, Fornecedor, etc)
- Máscara automática para CPF e CNPJ
- Busca por nome ou CPF
- Inclusão de múltiplos telefones
- Preenchimento automático de endereço via CEP
- Edição e exclusão de registros diretamente na tela
- Autenticação com login e senha
- Interface adaptada a desktop e celular/tablet

---

## ☁️ Sugestão de Deploy na Nuvem

Você pode publicar esta aplicação gratuitamente na nuvem usando a plataforma [Render](https://render.com). Siga os passos abaixo:

1. Crie uma conta gratuita no site [https://render.com](https://render.com)
2. Crie um novo **Web Service**
3. Conecte ao repositório GitHub contendo este projeto
4. Preencha os campos:

   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `bash start.sh`
   - **Root Directory**: (deixe em branco ou `Agenda1` se estiver dentro de pasta)

5. Certifique-se de que o arquivo `render.yaml` está presente para configuração automática (opcional)

> A aplicação será publicada com um link como `https://agenda-familiar.onrender.com`, acessível em qualquer celular, tablet ou computador com internet.



Você pode publicar esta aplicação gratuitamente em:

- [Render.com](https://render.com/)
- [Replit](https://replit.com/)
- [Firebase Hosting (Front-End)](https://firebase.google.com/)

Para isso, pode ser necessário adaptar o back-end para `render.yaml` ou contêiner com `Dockerfile`. Se quiser, posso gerar esse arquivo também.

---

## 📂 Firestore – Estrutura dos Dados

- **Coleção:** `pessoas`
- **Campos armazenados:**  
  - nome, sobrenome, tipo de pessoa, CPF/CNPJ (`fisco_id`), telefones[], endereço completo (rua, número, bairro, município, estado, país, CEP), data de nascimento
- **Chave:** ID único automático do Firestore

---

## 🧪 Testes de Responsividade

Para testar a aplicação em modo mobile:

1. Abra o navegador Chrome ou Edge
2. Acesse: `http://127.0.0.1:5000`
3. Pressione `F12` e ative o modo responsivo (ícone de celular/tablet)
4. Teste em larguras como 375px (iPhone) e 768px (tablet)

---

## 📱 Compatibilidade com Dispositivos Móveis

Esta aplicação foi atualizada para funcionar corretamente em **celulares e tablets**. As melhorias incluem:

- Inclusão da tag `<meta name="viewport">` em todos os arquivos HTML para ajustar a escala da tela.
- Uso de unidades relativas e centralização automática em formulários e campos de entrada.
- Aplicação de **media queries** nos arquivos CSS para garantir layout fluido em telas com largura inferior a 768px.

Essas mudanças permitem que a interface se adapte automaticamente, oferecendo uma melhor experiência para usuários móveis.
