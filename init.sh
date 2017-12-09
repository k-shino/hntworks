#/bin/bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y docker.io

sudo gpasswd -a ${USER} docker
sudo /bin/sh -c "curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
sudo chmod +x /usr/local/bin/docker-compose
sudo service docker restart


