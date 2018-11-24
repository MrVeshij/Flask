from app import app #  импорт экз класса фласк из модуля арр
import view # импорт модуля view
from app import db # имппорт БД

from posts.blueprint import posts # Из папки posts импорт блюпринта

app.register_blueprint(posts, url_prefix = '/blog')

if __name__ == '__main__':
	app.run(debug=True)