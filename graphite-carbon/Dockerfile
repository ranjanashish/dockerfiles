# Applications:
# [1] supervisor
# [2] carbon-cache

# Note: The official Debian images automatically ``apt-get clean`` after each ``apt-get``

FROM debian:jessie
MAINTAINER ranjanashish

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# pre-configure packages
RUN echo 'graphite-carbon graphite-carbon/postrm_remove_databases boolean false' | debconf-set-selections

# install packages
RUN apt-get update && apt-get -y install graphite-carbon supervisor

# graphite-carbon
ADD files/storage-schemas.conf     /etc/carbon/
ADD files/storage-aggregation.conf /etc/carbon/

# supervisor
ADD files/supervisord.conf /etc/supervisor/conf.d/

# data volumes
VOLUME ["/var/lib/graphite"]

# ports
EXPOSE 2003 2004 7002

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# default command
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
