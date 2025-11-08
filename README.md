# Репозиторий devices_api_tests

#### Для чего предназначен
Это форк репозитория https://github.com/HardTester/API_testing, на котором я практикуюсь в дописывании Python-API-автотестов в уже существующем проекте.


#### Запуск и установка 
```
git clone https://github.com/Atollye/devices_api_tests.git
sudo apt install python3-venv
python3 -m venv my_venv
source ./my_venv/bin/activate
pip install -r requirements.txt
pytest -v  ./tests
```


#### Библиотеки
httpx pytest pydantic python-dotenv allure