# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv(dotenv_path='<путь к файлу .env>')

# Теперь переменные доступны через os.environ
secret_key = os.getenv('SECRET_KEY')

print(secret_key) # Выведет: 12345
