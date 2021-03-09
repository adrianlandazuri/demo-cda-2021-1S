FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -yq
RUN apt-get install -yq  build-essential \
    python-dev \
    python3-minimal \
    python3-pip \
    python3-dev \       
    python3-venv

ENTRYPOINT bash