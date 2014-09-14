# Applications:
# [1] supervisord
# [2] memcached
# [3] postgresql
# [4] carbon-cache
# [5] uwsgi
# [6] nginx

# Note: The official Debian images automatically ``apt-get clean`` after each ``apt-get``

FROM debian:jessie
MAINTAINER ranjanashish

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# upgrade
RUN apt-get update && apt-get -y upgrade

# install essential packages
RUN apt-get -y install apt-utils dialog procps sudo

# pre-configure packages
RUN echo 'graphite-carbon graphite-carbon/postrm_remove_databases boolean false' | debconf-set-selections

# install packages
RUN apt-get -y install \
    graphite-carbon graphite-web \
    memcached python-memcache \
    nginx-full \
    uwsgi uwsgi-plugin-python \
    postgresql-9.4 postgresql-client-9.4 postgresql-contrib-9.4 libpq-dev python-psycopg2 \
    cron \
    supervisor

# postgres
RUN service postgresql start && \
    sudo -u postgres psql -c "CREATE USER graphite WITH PASSWORD 'password';" && \
    sudo -u postgres psql -c "CREATE DATABASE graphite WITH OWNER graphite;" && \
    service postgresql stop

# graphite-carbon
RUN sed -i 's/^\(CARBON_CACHE_ENABLED=\)false/\1true/' /etc/default/graphite-carbon
RUN sed -i 's/^\(ENABLE_LOGROTATION\s*=\s*\)False/\1True/' /etc/carbon/carbon.conf

# graphite-web
RUN sed -i "s/^#\(SECRET_KEY\s*=\s*'\)[^']*\('\)/\1$(< /dev/urandom tr -dc 'a-zA-Z0-9!#%^*()_+' | head -c 50)\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^#\(TIME_ZONE\s*=\s*'\)[^']*\('\)/\1Etc\/UTC\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^#\(MEMCACHE_HOSTS\s*=\s*\[\)[^]]*\(\]\)/\1'127.0.0.1:11211'\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'NAME':\s*'\)[^']*\(',\)/\1graphite\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'ENGINE':\s*'django.db.backends.\)[^']*\(',\)/\1postgresql_psycopg2\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'USER':\s*'\)[^']*\(',\)/\1graphite\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'PASSWORD':\s*'\)[^']*\(',\)/\1password\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'HOST':\s*'\)[^']*\(',\)/\1127.0.0.1\2/" /etc/graphite/local_settings.py
RUN service postgresql start && \
    graphite-manage syncdb --noinput && \
    service postgresql stop
RUN chown -R www-data:www-data /var/log/graphite
RUN touch /var/lib/graphite/search_index && chown www-data:www-data /var/lib/graphite/search_index

# uwsgi: application server
RUN rm -f /etc/uwsgi/apps-enabled/*
ADD files/graphite_web_uwsgi.ini /etc/uwsgi/apps-available/
RUN ln -sf /etc/uwsgi/apps-available/graphite_web_uwsgi.ini /etc/uwsgi/apps-enabled/graphite_web_uwsgi.ini

# nginx: web server
RUN rm -f /etc/nginx/sites-enabled/*
ADD files/graphite_web_nginx.conf /etc/nginx/sites-available/
RUN ln -sf /etc/nginx/sites-available/graphite_web_nginx.conf /etc/nginx/sites-enabled/graphite_web_nginx.conf
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf

# supervisor
ADD files/supervisord_event_listener.py /root/supervisord_event_listener.py
ADD files/supervisord.conf /etc/supervisor/conf.d/

# mount volumes
VOLUME /var/lib/graphite

# ports
EXPOSE 80
EXPOSE 2003 2004 7002

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# default command
CMD ["service", "supervisor", "start"]

