Изначально [рассматривал](google_cloud.md) Google Cloud, но при попытке регистрации выяснил, что они как и AWS, Microsoft, Hiroku) с марта 2022 года не принимают новые заявки из РФ.

Вообще, стоило начать со статьи "[Выбор оптимальной платформы для веб приложения](https://habr.com/ru/company/plesk/blog/548302/)", но нашёл её в самом конце сбора ссылок по Google Cloud, Yandex Cloud и хостингам.



# Альтернатива 1, wip: Yandex Cloud

TODO: сохранить пачку ссылок с доков по созданию аккаунта и началу деплоя.

## Офф. документация

### Начало работы

[Руководства по работе с веб-сервисами в Yandex Cloud](https://cloud.yandex.ru/docs/tutorials/web/) (про контейнеры и Python прямым отдельного топика нет, см. гайды ниже).

Про контейнеры --[Yandex Serverless Containers](https://cloud.yandex.ru/docs/serverless-containers/) 

[Создание виртуальной машины Linux](https://cloud.yandex.ru/docs/compute/quickstart/quick-create-linux)

### Тарификация

[Правила тарификации для Compute Cloud](https://cloud.yandex.ru/docs/compute/pricing)

[Калькулятор цен](https://cloud.yandex.ru/prices)

[Правила тарификации для Serverless Containers](https://cloud.yandex.ru/docs/serverless-containers/pricing)

[Free Tier](https://cloud.yandex.ru/docs/billing/concepts/serverless-free-tier#serverless-containers)

[Правила тарификации для бессерверного режима Managed Service for YDB (запросы к БД)](https://cloud.yandex.ru/docs/ydb/pricing/serverless)

## Гайды

[Yandex Compute Cloud + Docker + Python + Flask. Разворачиваем веб приложение (видео)](https://www.youtube.com/watch?v=fCQ8ogMHSoo)

[Python + Flask + Docker + Nginx + PostgreSQL + Git + Yandex Cloud. Разворачиваю веб приложение (видео)](https://www.youtube.com/watch?v=w7Sx_QNCekE)

## Прочее

[Yappa: запускаем python web-приложения. Просто. Бессерверно. В Яндекс Облаке](https://habr.com/ru/post/569674/)


# Альтернатива 2, wip: платные хостинги

**Идея**, wip: хостинг -- 1 VM -- несколько веб-приложений на 1 IP

Контекст:
- [Хостинг нескольких сайтов на одном Google Cloud Computer Engine](https://medium.com/google-cloud/hosting-multiple-websites-on-single-google-cloud-compute-engine-9768e2f02c6d);
-[How to Run Multiple WordPress Websites on One Nginx Server](https://tonyteaches.tech/run-multiple-wordpress-websites-on-one-server/).

Искал под Pyhton:
-[варианты 1](https://hostinghub.ru/top/tech/python) 
-[варианты 2](https://ru.hostadvice.com/python-hosting/) 

# Бесплатные хостинги

Материалы:
- [Список бесплатных сервисов](https://free-for.dev/#/) может здесь пригодиться. 
-[Бесплатные хостинги для веб-разработчиков (от 12-2020)](https://habr.com/ru/post/535168/) 
