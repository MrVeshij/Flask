class Configuration(): # Конфигурации которые читаются и применяются в арр 
	DEBUG = True # режим дебага, можно кодить сразу наблюдая изменения в сервере
	SQLALCHEMY_TRACK_MODIFICATIONS = False # снимает предупреждающую строку в сервере при работе
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/test1' # Указываем базу данных и место обращения к данным
	SECRET_KEY = 'secret key must be secret'