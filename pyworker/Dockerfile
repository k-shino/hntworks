FROM ubuntu:16.04

maintainer "k-shino" <nocknocknock@gmail.com>

RUN apt-get update -qq \
  && apt-get upgrade -qy \
  && apt-get install -qy python3 git python3-pip python3-dev python-setuptools build-essential python-dev libev4 libev-dev make g++ wget git stress iproute2 vim iputils-ping net-tools \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && easy_install cassandra-driver

ENV CQLSH_VERSION 5.0.3
RUN git clone https://github.com/nabebugyo/elg.git
RUN pip3 install pandas
RUN pip3 install cqlsh==5.0.3

CMD tail -f /dev/null
