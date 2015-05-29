# Applications:
# [1] supervisor
# [2] elasticsearch

FROM debian:jessie
MAINTAINER ranjanashish

ENV ES_VERSION 1.5
ENV ES_PORT 9200

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install packages
RUN apt-get update && apt-get -y install openjdk-7-jre supervisor wget

# install elasticsearch
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    echo "deb http://packages.elastic.co/elasticsearch/${ES_VERSION}/debian stable main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y install elasticsearch

# supervisor
ADD files/supervisord.conf /etc/supervisor/conf.d/

# mount volumes
VOLUME /var/lib/elasticsearch

# ports
EXPOSE ${ES_PORT}

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# default command
CMD ["service", "supervisor", "start"]

