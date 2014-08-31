# Applications:
# [1] memcached
# [2] postgresql
# [3] carbon-cache
# [4] nginx

FROM debian:jessie
MAINTAINER ranjanashish

# upgrade
RUN apt-get update
RUN apt-get -y install apt-utils dialog
RUN apt-get -y upgrade

# install essential packages
RUN apt-get -y install procps sudo

# pre-configure packages
RUN echo graphite-carbon graphite-carbon/postrm_remove_databases boolean false | debconf-set-selections

# install packages
RUN apt-get -y install graphite-carbon graphite-web memcached python-memcache nginx postgresql libpq-dev python-psycopg2

# postgres
RUN service postgresql start
RUN sudo -u postgres psql -c "CREATE USER graphite WITH PASSWORD 'password';"
RUN sudo -u postgres psql -c "CREATE DATABASE graphite WITH OWNER graphite;"

# graphite-carbon
RUN sed -i 's/CARBON_CACHE_ENABLED=false/CARBON_CACHE_ENABLED=true/' /etc/default/graphite-carbon

# graphite-web
RUN sed -i "s/^#\(SECRET_KEY\s*=\s*'\)[^']*\('\)/\1$(< /dev/urandom tr -dc 'a-zA-Z0-9!#%^*()_+' | head -c 50)\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^#\(TIME_ZONE\s*=\s*'\)[^']*\('\)/\1Etc\/UTC\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^#\(MEMCACHE_HOSTS\s*=\s*\[\)[^]]*\(\]\)/\1'127.0.0.1:11211'\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'NAME':\s*'\)[^']*\(',\)/\1graphite\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'ENGINE':\s*'django.db.backends.\)[^']*\(',\)/\1postgresql_psycopg2\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'USER':\s*'\)[^']*\(',\)/\1graphite\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'PASSWORD':\s*'\)[^']*\(',\)/\1password\2/" /etc/graphite/local_settings.py
RUN sed -i "s/^\(\s*'HOST':\s*'\)[^']*\(',\)/\1127.0.0.1\2/" /etc/graphite/local_settings.py
RUN graphite-manage syncdb --noinput

# nginx
ADD graphite-web /etc/nginx/sites-available/
RUN rm -f /etc/nginx/sites-enabled/default
RUN ln -sf /etc/nginx/sites-available/graphite-web /etc/nginx/sites-enabled/graphite-web

# mount volumes
VOLUME /var/lib/graphite

# ports
EXPOSE 80
EXPOSE 2003 2004 7002

# clean
RUN apt-get -y clean
