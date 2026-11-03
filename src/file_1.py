# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv(dotenv_path='key.env')

# Теперь переменные доступны через os.environ
secret_key = os.getenv('SECRET_KEY')
author = os.getenv('AUTHOR_1')

def print_author():
# Допишите здесь ваш код
   print(f"Автор проекта: {author}")

print(secret_key) # Выведет: 12345
print_author()
