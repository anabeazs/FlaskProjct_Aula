from aplicacao import app, database, bcrypt
from flask import redirect, render_template, url_for, flash
from aplicacao.forms import FormLogin, FormCadastrarUsuario
from aplicacao.forms import FormLogin, FormCadastrarUsuario
from aplicacao.models import Usuario
from flask_login import login_user, logout_user



@app.route('/', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(usuario=form.usuario.data).first()
        print(user.senha)
        print(form.senha.data)
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user, remember=form.lembrar.data)
            flash(f'Login feito com sucesso para o user: {form.usuario.data}', 'alert alert-success')
            return redirect(url_for('produtos'))
        else:
            flash(f'Usuario ou senha inválidos', 'alert alert-danger')
    return render_template('login.html', form=form)

@app.route('/sair')
def sair():
    logout_user()
    flash(f'Sessão encerrada', 'alert alert-info')
    return redirect(url_for('login'))

@app.route('/cadastro-usuario',  methods=['GET', 'POST'])
def cadastro_usuario():
    form = FormCadastrarUsuario()
    if form.validate_on_submit():
        senha_crypto= bcrypt.generate_password_hash(form.senha.data)

        user = Usuario(usuario=form.usuario.data, email=form.email.data, senha=senha_crypto)
        database.session.add(user)
        database.session.commit()
        return redirect('produtos')
    return render_template('cadastrar_usuario.html', form=form)

@app.route('/produtos')
def produtos():
    produtos = ['Caneca', 'Caneta', 'Caderno', 'TV', 'Notebook']
    return render_template('lista_produto.html', nomes=produtos)
