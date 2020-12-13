    # Лабораторна робота №4: Робота з Docker

+ Мною було створено файл `my_work.log`
```
(docker -v; docker --help; docker run docker/whalesay cowsay Docker is fun;) > my_work.log
```

+ Забілдив імедж із `Dockerfile`
```
docker build -t yuriidiuklab4:django .
```
+ Перевірив наявні імеджі
```
docker images
```

+ Запустив створений Docker-імедж
```
docker run -it -p 8000:8000 yuriidiuk/lab4:django
```

+ Забілдив новий імедж
```
docker build -t yuriidiuk/lab4:monitoring -f Dockerfile.monitoring . 
```

+ Запустив моніторинг
```
docker run -it yuriidiuk/lab4:monitoring
```
+ Імеджі завантажив на `DockerHub`

```
docker push yuriidiuk/lab4:django
docker push yuriidiuk/lab4:monitoring
```

+ Запустив моніторинг імеджа із підключеним томом:
```
docker run -it --net=host -v /home/ubuntu/Desktop/lab4:/app/ yuriidiuk/lab4:monitoring
```

### Мій [Докер профіль](https://hub.docker.com/u/yuriidiuk)
### Мій [Докер репозиторій](https://hub.docker.com/repository/docker/yuriidiuk/lab4)