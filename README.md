Тестове завдання
Junior Python Developer

Опис завдання

Необхідно розробити простий додаток для управління
IoT пристроями на Python.

## install

1. Clone repo:
  --Clone with SSH `git@github.com:Danil1994/iot_devices.git`
  --Clone with HTTPS `https://github.com/Danil1994/iot_devices.git`

2. Go to your project folder: `path/to/the/folder`
3. Load your .env file to the project.
4. Install requirements.txt run: `pip install -r requirements.txt`
5. Create database and configure connection parameters

## Run

1. Run server: `python app.py`
2. Go to link `http://127.0.0.1:8080/devices` in your browser.

## Using



Управління базою даних:
1. Налаштуйте базу даних PostgreSQL.
2. Створіть необхідні таблиці:
• api_user (name, email, password)
• device (name, type, login, password, location_id, api_user_id)
• location (name)
3. Для взаємодії з базою даних з додатку використовуйте бібліотеку peeweе

Розробка API:
1. Створіть асинхронний API з використанням бібліотеки aiohttp.
2. Реалізуйте операції CRUD: додавання, читання, оновлення і видалення пристроїв.
Додаткові функції:
1. Створіть Docker-контейнер для зручнішого розгортання додатку.
2. Покрийте тестами код
3. Додайте логування дій та помилок
4. 
Якість коду та документація:
1. Напишіть чистий, структурований код, який відповідає найкращим практикам.
2. Додайте необхідну документацію для налаштування та запуску додатку.
Подання:
