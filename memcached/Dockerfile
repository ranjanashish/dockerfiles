# Applications:
# [1] supervisor
# [2] memcached

FROM debian:jessie
MAINTAINER ranjanashish

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install packages
RUN apt-get update && apt-get -y install memcached supervisor

# supervisor
ADD files/supervisord.conf /etc/supervisor/conf.d/

# ports
EXPOSE 11211

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections    

# default command
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
