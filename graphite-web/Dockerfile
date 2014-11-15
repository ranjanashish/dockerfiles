# Applications:
# [1] supervisor
# [2] postgresql
# [3] uwsgi
# [4] nginx

# Note: The official Debian images automatically ``apt-get clean`` after each ``apt-get``

FROM debian:jessie
MAINTAINER ranjanashish

# debconf frontend: noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install packages
RUN apt-get update && apt-get -y install \
    cron sudo \
    graphite-web \
    python-memcache \
    nginx-full \
    uwsgi uwsgi-plugin-python \
    postgresql-9.4 postgresql-client-9.4 libpq-dev python-psycopg2 \
    supervisor

# postgres
ADD files/graphite_web_user_db.sql /tmp/
RUN service postgresql start && \
    sudo -u postgres psql -f /tmp/graphite_web_user_db.sql && \
    service postgresql stop && \
    rm -f /tmp/graphite_web_user_db.sql

# graphite-web
ADD files/local_settings.py /etc/graphite/
RUN sed -i "s/^#\(SECRET_KEY\s*=\s*'\)[^']*\('\)/\1$(< /dev/urandom tr -dc 'a-zA-Z0-9!#%^*()_+' | head -c 50)\2/" /etc/graphite/local_settings.py

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

# ports
EXPOSE 80

# debconf frontend: dialog
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# default command
CMD ["service", "supervisor", "start"]
