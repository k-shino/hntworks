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
RUN git clone https://github.com/nabebugyo/elg.git \
  && pip3 install pandas cqlsh==5.0.3 \
  && cp -r /usr/local/lib/python3.5/dist-packages/cqlshlib /usr/local/lib/python2.7/dist-packages/cqlshlib

COPY init_db.py /

CMD python /init_db.py; tail -f /dev/null
