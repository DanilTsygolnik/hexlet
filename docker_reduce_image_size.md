## Как уменьшить размер docker image

Привлекательным решением выглядит утилита [docker-slim](https://dockersl.im/install.html).

Простая установка[^docker-slim-install]
```
tar -zvxf dist_linux.tar.gz
# убедиться, что /usr/local/bin входит в $PATH
$PATH
# установка
sudo cp dist_linux/* /usr/local/bin
# проверка
which docker-slim
docker-slim help
```

[^docker-slim-install]: https://linuxways.net/centos/dockerslim-to-minify-optimize-and-secure-docker-container-in-linux/

Image, который будем сжимать должен заранее быть загружен:
```
docker pull <image>
docker images  # должно быть в списке
```

Базовая команда для сжатия -- `docker-slim build --target <image>`

[Подробно о командах](https://github.com/docker-slim/docker-slim#usage-details).

#### Удачный опыт

Для эксперимента скачал cowsay.

Размеры до и после:
```
REPOSITORY              TAG         IMAGE ID       CREATED          SIZE
rancher/cowsay          latest      8fe7792ad843   21 months ago    39.9MB
rancher/cowsay.slim     latest      a5c4b7134065   7 seconds ago    5.49MB
```

Прошло с заминкой, по коду ошибки нашел решение[^cowsay-sol]:
`docker-slim build --http-probe=false --target rancher/cowsay`

[^cowsay-sol]: https://github.com/docker-slim/docker-slim/issues/235#issuecomment-954074079

Запись сессии в терминале:
[![asciicast](https://asciinema.org/a/eOhZD2tQJX4Jh7Kw1uiJ7sytK.svg)](https://asciinema.org/a/eOhZD2tQJX4Jh7Kw1uiJ7sytK)

---

Image с web-приложением на Python ужать не получилось.

[![asciicast](https://asciinema.org/a/7Jg8t77cdYnlsSdgb4cD5voIt.svg)](https://asciinema.org/a/7Jg8t77cdYnlsSdgb4cD5voIt)

[Говорят](https://stackoverflow.com/questions/62146402/how-to-optimize-a-docker-image), что большой размер контейнеров с кодом на Python - норма. Внутри ещё ссылки по вопросу.

[Reducing the size of a Python application Docker image using Python wheels](https://www.peterspython.com/en/blog/reducing-the-size-of-a-python-application-docker-image-using-python-wheels) - подробное описание с кодом.

[How to reduce Docker Image sizes using multi-stage builds](https://blog.logrocket.com/reduce-docker-image-sizes-using-multi-stage-builds/) - частично перекликается с предыдущей статьей (??).
