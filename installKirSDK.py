import os
from git import Repo

#Логика установки
print('Программа установки KirSDK')
print('Клонирование репозитория: PyCode...')
if not os.path.exists('PyCode'):
    os.makedirs('PyCode')
Repo.clone_from("https://github.com/Kirillovo-Company/pycode", "PyCode")
print('Установка завершена')
