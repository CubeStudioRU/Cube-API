<h1 align="center">
  <img src="images/banner.svg" alt="Cube API"/>
  Cube API
  <br/>
</h1>

<p align="center">
    Rest API, которое используется в сервисах CubeStudio.
</p>

## Дорожная карта Cube-API
* [X] Первый запуск Cube-API
* [X] Добавить поддержку CurseForge
* [X] Создание Dockerfile, docker-compose, контейнеризация Cube-API
* [ ] Создать Cube-CLI
* [ ] Додавить поддержку своих модов
* [ ] Добавить поддержку множества Instances одновременно
* [ ] Добавить обновление различных конфигов
* [ ] Поддержка будущего CubeBadges*

## Стек проекта
* ```FastAPI```
* ```uvicorn```
* ```Pydantic```

## Полезные ссылки
* Телеграм-канал CubeStudio: https://t.me/+Gphg_BIJEdMwMmFi
* Сайт CubeStudio: [fadegor05.github.io/CubeStudio/](https://fadegor05.github.io/CubeStudio/)
* CubeStart: https://github.com/fadegor05/Cube-Start

## Как работают Instance?
Что такое Instance? Instance - это один из новых уникальных и простых способов передачи сборки на устройство участника проекта CubeShield, настройка сборки происходит в файле ```instance.json```, который обязательно должен находится в корневой папке проекта, этот файл имеет данное содержание:
```
{
  "id": 0, // Айди проекта (Необходимо менять для каждой новой сборки)
  "name": "CubeShield Experiment: Example", // Название сборки
  "version": "0.0.1", // Версия сборки (Необходимо менять для применения изменений для всех игроков)
  "changelog": "", // Изменения версии
  "game_version": "1.20.4", // Версия Minecraft
  "loader": "fabric", // Загрузчик Minecraft
  "modrinth": [ // Моды с сайта Modrinth
    {
      "mod": "simple-voice-chat", // Slug или ID мода
      "version": "fabric-1.20.4-2.5.1" // Slug или ID версии мода (все можно найти в строке поиска, при открытом моде)
    },
    {
      "mod": "...",
      "version": "..."
    },
  ],
  "curseforge": [ // Моды с сайта CurseForge
    {
      "mod": "structurize" // Не обязательно (для более простого определения мода при составлении instance.json)
      "mod_id": 298744, // ID мода
      "file_id": 5082629 // ID версии мода (все можно найти в строке поиска, при открытом моде)
    },
    {
      "mod": "...",
      "mod_id": ...,
      "file_id": ...
    },
  ]
}
```

## Переменные среды
```CURSEFORGE_API_KEY =  ...``` - API ключ для доступа к сервисам CurseForge

```API_KEY = ...``` - секретный ключ для будующих интеграций

## Деплой (Development)
```
git clone https://github.com/fadegor05/Cube-API.git
```
Клонирование репозитория Cube-API
```
poetry update
```
Подтягивание зависимостей Poetry
```
poetry run uvicorn app:create_app --port 8000
```
Запуск Cube-API в режиме разработки

## Деплой (Production)
Клонирование репозитория Cube-API
```
git clone https://github.com/fadegor05/Cube-API.git ~/cube-api
```
Перемещение в директорию репозитория
```
cd ~/cube-api
```
Создание директорий для хранения конфигов, сборок, Docker volume
```
mkdir ~/cube-api-config ~/cube-api-config/instance
```
Копирование конфига в директорию с конфигами для Docker
```
cp ~/cube-api/instance_template.json ~/cube-api-config/instance/instance.json
```
Изменение файла конфигурации текущей сборки
```
nano ~/cube-api-config/instance/instance.json
```
Настройка окружения для API ключей
```
nano ~/cube-api/.env
```
Сборка, запуск контейнера в фоновом режиме
```
docker-compose up --build --detach
```
Остановка контейнера
```
docker container stop cube-api
```

###### Not an official Minecraft product. We are in no way affiliated with or endorsed by Mojang Synergies AB, Microsoft Corporation or other rightsholders.