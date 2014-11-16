# Applications:
# [1] supervisor
# [2] nginx

FROM debian:jessie
MAINTAINER ranjanashish

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install packages
RUN apt-get update && apt-get -y install nginx-full supervisor wget

# install grafana
RUN wget -P /tmp http://grafanarel.s3.amazonaws.com/grafana-1.8.1.tar.gz && \
    tar -xzf /tmp/grafana-1.8.1.tar.gz -C /usr/share/nginx/html && \
    rm -f /tmp/grafana-1.8.1.tar.gz && \
    mv /usr/share/nginx/html/grafana-1.8.1 /usr/share/nginx/html/grafana

# grafana
ADD files/config.js /usr/share/nginx/html/grafana/

# nginx: web server
RUN rm -f /etc/nginx/sites-enabled/*
ADD files/grafana_nginx.conf /etc/nginx/sites-available/
RUN ln -sf /etc/nginx/sites-available/grafana_nginx.conf /etc/nginx/sites-enabled/grafana_nginx.conf
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf

# supervisor
ADD files/supervisord.conf /etc/supervisor/conf.d/

# ports
EXPOSE 80

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# default command
CMD ["service", "supervisor", "start"]
