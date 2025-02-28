Для запуска приложения необходимо создать файл ".env" и установить в него переменные окружения:
- DB_HOST
- DB_PORT
- DB_USER
- DB_PASS
- DB_NAME
- APP_PORT

Выполнить команду:
    
    docker compose up --build
    
После разворачивания контейнеров можно выполнить миграции

    alembic revision --autogenerate -m 'initial'

    alembic upgrade head

