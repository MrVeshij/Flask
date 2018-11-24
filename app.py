from flask import Flask   # импорт модуля фласк из внешней библиотеки
from config import Configuration # импорт модуля конфиг из папки в которой лежит app.py 
from flask_sqlalchemy import SQLAlchemy # Импорт модуля связующего базу данных с фласком


from flask_migrate import Migrate, MigrateCommand # модуль отвечающий за обновления баз данных
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__) # Создаем экземпляр класса Flask передавая ему имя документа из которого идет запись (app)
app.config.from_object(Configuration) # В атрибут арр записываем новый объект списка

db = SQLAlchemy(app) # экземпляр класса отвечающий за доступ к базе данных

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *
### ADMIN ###
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))