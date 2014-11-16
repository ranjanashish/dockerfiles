# Applications:
# [1] supervisor
# [2] elasticsearch

FROM debian:jessie
MAINTAINER ranjanashish

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install packages
RUN apt-get update && apt-get -y install openjdk-7-jre supervisor wget

# install elasticsearch
RUN wget -qO - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add - && \
    echo 'deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main' >> /etc/apt/sources.list
RUN apt-get update && apt-get -y install elasticsearch

# supervisor
ADD files/supervisord.conf /etc/supervisor/conf.d/

# mount volumes
VOLUME /var/lib/elasticsearch

# ports
EXPOSE 9200

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# default command
CMD ["service", "supervisor", "start"]
