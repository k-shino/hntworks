FROM ubuntu:16.04

maintainer "shinohara" <nocknocknock@gmail.com>

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 git python3-pip

RUN git clone https://github.com/nabebugyo/elg.git
RUN pip3 install pandas

