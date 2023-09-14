# Проект для тестирования REST и gRPC API сервиса DM API Account


### Ответственные лица:

* Меньшиков Валерий:
  * telegram: [Valeriy Menshikov](https://t.me/valeriy_menshikov)

  

### Тестируемый сервис:
**dm_api_account**
* Swagger: [swagger](http://5.63.153.31:5051/index.html?urls.primaryName=Account)


### Установка и запуск
```shell
 git clone https://github.com/ValeriyMenshikov/rest_api_tests
 cd rest_api_tests
 pip install -r requirements.txt
```

### Docker
```shell
docker build -t rest_api_tests . 
docker run -it --rm rest_api_tests
```

### Различия в ветках фреймворка
В ветке main - фреймворк, который включает в себя все вспомогательные библиотеки.  
В ветке client - фреймворк, из которого вынесены вспомогательные библиотеки.  
В ветке client_gen - фреймворк, где клиент account и login сгенерированы, а так же сгенерирован клиент из gRPC модели.  

### Используемые технологии
<p  align="center">
  <code><img width="5%" src="images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" src="images/logo_stacks/python.png"></code>
  <code><img width="5%" src="images/logo_stacks/pytest.png"></code>
  <code><img width="5%" src="images/logo_stacks/postman.png"></code>
  <code><img width="5%" src="images/logo_stacks/docker.png"></code>
  <code><img width="5%" src="images/logo_stacks/requests.png"></code>
  <code><img width="5%" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" src="images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" src="images/logo_stacks/grpc.png"></code>
  <code><img width="5%" src="images/logo_stacks/openapi.png"></code>
</p>

### Архитектура проекта

```
 ├── configs                     # Папка со всей конфигурацией проекта
 │   ├── prod.yml                # Настройки для прода
 │   └── stg.yml                 # Настройки для тестовой среды
 ├── data                        # Папка для констант и статических тестовых данных
 │   └── post_v1_account.py      # Файл где должны храняться константы для метода создания аккаунта
 ├── modules                     # Папка с сырыми клиентами сервисов
 │   ├── grpc                    # gRPC клиенты
 │   ├── http                    # http клиенты
 │   └── db                      # db клиенты
 ├── common                      # Папка для констант и статических тестовых данных
 │   ├── db_client               # Клиент с логгированием для работы с базой данных
 │   ├── orm_client              # Клиент с логгированием для работы с базой данных через ORM
 │   └── rest_client             # Клиент с логгированием для работы REST API
 ├── generic                     # Папка с базовыми специфичными для проекта проверочными и вспомогательными классами и функциями
 │   ├── helpers                 # Папка для вспомогательного функционала общего назначения 
 │   │   ├── account.py          # Помощник для работы с account_api
 │   │   ├── login.py            # Помощник для работы с login_api
 │   │   └── search.py           # Помощник для работы с gRPC сервисом
 │   ├── assertions              # Папка для проверок
 │   │   └── post_v1_account.py  # Файл содержит assert-ы для метода post_v1_account
 ├── tests                       # Папка для хранения тестов
 │   ├── test_account            # Папка с тестами для account_api
 │   ├── test_login              # Папка с тестами для login_api
 │   └── test_search             # Папка с тестами для search gRPC API
 ├── .gitignore                  # Стандартный файл для игнорирования нежелательных файлов для загрузки в репозиторий
 ├── conftest.py                 # Файл с инициализацией настроек и фикстур
 ├── requirements.txt            # Файл с зависимостями
 └── README.md                   # Файл с описанием репозитория для тестов
```
### В файле config настраиваются окружения и выносятся основные подключения.
![This is an image](images/screenshots/config.png)



### <img width="3%" title="Allure Report" src="images/logo_stacks/allure_report.png"> Allure report
##### После прохождения тестов, результаты можно посмотреть в генерируемом Allure отчете.
![This is an image](images/screenshots/allure-report.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure-graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и добавлены логи.
![This is an image](images/screenshots/allure-suites.png)


