## Установка

Порядок установки Docker в Manjaro[^manjaro-install-docker].

[^manjaro-install-docker]: https://linuxconfig.org/manjaro-linux-docker-installation

```
# install docker
sudo pacman -Syu docker
# start the Docker service
# from now on docker command must be working
sudo systemctl start docker.service
# enable Docker service to run whenever the system is rebooted
sudo systemctl enable docker.service
# verify docker installation
sudo docker version
sudo docker info

# provide the ability to run Docker as the current user
sudo usermod -aG docker $USER
# reboot your system for those changes to take effect
reboot
```

После перезагрузки команда            
`docker run hello-world`        
должна привести к следующему выводу:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
