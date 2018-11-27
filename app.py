from flask import Flask   # импорт модуля фласк из внешней библиотеки
from config import Configuration # импорт модуля конфиг из папки в которой лежит app.py 
from flask_sqlalchemy import SQLAlchemy # Импорт модуля связующего базу данных с фласком


from flask_migrate import Migrate, MigrateCommand # модуль отвечающий за обновления баз данных
from flask_script import Manager

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

from flask import redirect, url_for, request

app = Flask(__name__) # Создаем экземпляр класса Flask передавая ему имя документа из которого идет запись (app)
app.config.from_object(Configuration) # В атрибут арр записываем новый объект списка

db = SQLAlchemy(app) # экземпляр класса отвечающий за доступ к базе данных

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *
### ADMIN ###

class AdminView(ModelView):
	def is_accessible(self):
		return current_user.has_role('admin')

	def inaccessible_callback(self, name, **kwargs):
		return redirect( url_for('security.login', next=request.url ))


class HomeAdminView(AdminIndexView):
	def is_accessible(self):
		return current_user.has_role('admin')

	def inaccessible_callback(self, name, **kwargs):
		return redirect( url_for('security.login', next=request.url ))


admin = Admin(app, 'FlaskApplication', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Tag, db.session))

###Flask-security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
