<h1 align="center">
  <img src="images/banner.svg" alt="Cube API"/>
  Cube API
  <br/>
</h1>

<p align="center">
    Rest API, которое используется в сервисах CubeStudio.
</p>

## Стек

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

## Дорожная карта Cube-API

* [X] Первый запуск Cube-API
* [X] Поддержка CurseForge
* [X] Dockerfile, docker-compose, контейнеризация Cube-API
* [ ] Поддержка сторонних сервисов (например, Yandex.Drive, Google.Drive, Dropbox и т.д.)
* [ ] Добавление скачивания некоторых файлов напрямую с Cube-API, например конфигов
* [ ] Возможность наличия нескольких обновляемых Instances

## Полезные ссылки

* Телеграм-канал CubeStudio: https://t.me/+Gphg_BIJEdMwMmFi
* Сайт CubeStudio: [fadegor05.github.io/CubeStudio/](https://fadegor05.github.io/CubeStudio/)
* CubeStart: https://github.com/fadegor05/CubeStart

## Как работают Instance?

Что такое Instance? Instance — это исчерпывающие описание сборки Minecraft, содержащей в себе моды разных сервисов.

**Коллекция** `instances`:

```
{
  "uuid": "0", // Индификатор проекта
  "name": "CubeShield Experiment: Example", // Название сборки
  "version": "0.0.1", // Версия сборки
  "changelog": "", // Изменения версии
  "game_version": "1.20.4", // Версия Minecraft
  "loader": "fabric", // Загрузчик Minecraft
  "modrinth": [ // Моды с сайта Modrinth
    {
      "mod": "simple-voice-chat", // Slug или ID мода
      "version": "fabric-1.20.4-2.5.1", // Slug или ID версии мода (все можно найти в строке поиска, при открытом моде)
      "side": "client" // Только для сервера (server), только для клиента (client), везде (both)
    },
    {
      "mod": "...",
      "version": "...",
      "side": "..."
    },
  ],
  "curseforge": [ // Моды с сайта CurseForge
    {
      "mod": "structurize" // Не обязательно (для более простого определения мода при составлении instance.json)
      "mod_id": 298744, // ID мода
      "file_id": 5082629 // ID версии мода (все можно найти в строке поиска, при открытом моде)
      "side": "both" // Только для сервера (server), только для клиента (client), везде (both)
    },
    {
      "mod": "...",
      "mod_id": ...,
      "file_id": ...,
      "side": ...
    },
  ]
}

```

## Переменные среды

```
CURSEFORGE_API_KEY= # Ключ CurseForge Studios
BACKEND_PORT=8000 # Порт API

MONGO_ROOT_USER= # Логин MongoDB
MONGO_ROOT_PASS= # Пароль MongoDB
MONGO_PORT=4000 # Порт MongoDB
```

## Деплой

Клонирование репозитория Cube-API

```
git clone https://github.com/fadegor05/Cube-API.git
```

Перемещение в директорию репозитория

```
cd Cube-API
```

Сборка, запуск контейнера в фоновом режиме

```
docker-compose up --build -d
```

Остановка контейнера

```
docker container stop cube-api
```

###### Not an official Minecraft product. We are in no way affiliated with or endorsed by Mojang Synergies AB, Microsoft Corporation or other rightsholders.
