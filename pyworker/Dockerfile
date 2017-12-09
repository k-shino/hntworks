FROM ubuntu:16.04

maintainer "k-shino" <nocknocknock@gmail.com>

RUN apt-get update -qq && apt-get upgrade -qy && apt-get install -qy python3 git python3-pip
RUN apt-get install -qy make g++ wget git stress iproute2 vim iputils-ping net-tools

RUN git clone https://github.com/nabebugyo/elg.git
RUN pip3 install pandas

RUN apt install -qy python-setuptools build-essential python-dev libev4 libev-dev
RUN easy_install cassandra-driver

CMD tail -f /dev/null
