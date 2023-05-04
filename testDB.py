from aplicacao import app, database, bcrypt
from aplicacao.models import Usuario

'''Cria e deleta o banco de dados'''
with app.app_context():
    database.drop_all()
    database.create_all()

'''insere um usuario inicial na base de dados'''
with app.app_context():
    senha_crypto = bcrypt.generate_password_hash('123456')
    user = Usuario(usuario='admin', email = 'adm@gmail.com', senha = senha_crypto)
    database.session.add(user)
    database.session.commit()


# with app.app_context():
#     usuarios = Usuario.query.all()
#     for item in usuarios:
#         print(f"{item.usuario}, {item.email}, {item.senha}")

