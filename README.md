## install

1. Clone repo:

* Clone with SSH `git clone git@github.com:Danil1994/iot_devices.git`.
* Clone with HTTPS `git clone https://github.com/Danil1994/iot_devices.git`.

2. Go to your project folder: `path/to/the/folder`.
3. Load your .env file to the project like .env.example.
4. Install requirements.txt run: `pip install -r requirements.txt`.
5. Create database and configure connection parameters.
6. Run `python create_fake_data.py` to create fake data.

## Run

1. Run server: `python app.py`
2. Go to link `http://127.0.0.1:8080/api/v1/doc#/Devices` in your browser.

## Using

Приложение поддерживает базовые CRUD операции.

* GET `/devices` retrieve all devices.
* POST `/devices` create a new device.
* GET `/devices/{id}` get a device by ID.
* PUT `/devices/{id}` update an existing device.
* DELETE `/devices/{id}` delete a device by ID.
