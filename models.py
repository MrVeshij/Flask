from app import db
from datetime import datetime
import re # модуль отвечает за работу с регулярными выражениями

def slugify(s): # Функция перерабатывает строку возвращая только те символы, которые будут использоваться в поисковой строке
	pattern = r'[^\w+]' # r перед строкой говорит о том что всю строку нужно воспринять буквально|либо там есть какой то свой смысл|проверить в тестах самой функции
	return re.sub(pattern, '-', str(s)) # символы из переменной патерн заменяет на дефис в выражении s

post_tags = db.Table('post_tags', # создается база данных ответственная за связь таблицы Тэг и таблицы Пост
			db.Column('post_id',db.Integer, db.ForeignKey('post.id')), # поле с числовым значением if поста
			db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')) # поле с числовым значением if тэга
	)



class Post(db.Model): # Данные при создании поста, формируются ряд колонок
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.generate_slug()

	tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic')) # создает переменную "отношений" через которую возможно получить объект BaseQuery для простоты использования поиска по например статьям

	def generate_slug(self):# Генерация логики заголовков
	# Слаг в админки создается вручну, и никак не создается если его не указать явно (Разобрать, почему)
		if self.title:
			self.slug = slugify(self.title)
	
	def __repr__(self):
		return '<Post id: {}, title: {}>'.format(self.id, self.title)

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	slug = db.Column(db.String(100))

	def __init__(self, *args, **kwargs):
		super(Tag, self).__init__(*args,**kwargs)
		self.slug = slugify(self.name) #slugify(self.name) если оставить этот параметр то при создании тэга с записью через админку
		# Вываливается ошибка что тип данных не совпадает с ожидаемым, якобы функция slugify вовзращает не string что проверив через я опровергнул
		# для временного решения я просто записываю в слаг по умолчанию имя(title) тэга
		# Впоследствии это может привести к пробленым слагом по которым не будут читаться тэги
		# К 10 и 11 уроку приводятся причины и варианты реализации этой проблемы
	def __repr__(self):
		return '<Tag id: {}, name: {}>'.format(self.id, self.name)
