graphite
========

Base Image - debian:jessie

Applications
------------
1. supervisor   - for smartly managing all applications running in this docker image
2. memcached    - for caching content of graphite-web (improves performace of graphite-web tremendously)
3. postgresql   - for database of graphite-web (saving dashboards etc.)
4. carbon-cache - for listening to time-series data (another docker image can be used for statsd)
5. uwsgi        - for serving non-static-content (django) requests of graphite-web
6. nginx        - for serving static-content requests of graphite-web and forwarding non-static-content (django) requests to uwsgi

Advantages
----------
* Uses supervisor for process management
* Uses memcached for better performace of graphite-web
* Uses postgresql instead of sqlite
* Uses /var/lib/graphite as a data volume

Beginners
---------
uWSGI
* https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html
* http://uwsgi-docs.readthedocs.org/en/latest/Vars.html

Supervisor
* http://supervisord.org/configuration.html
* http://supervisord.org/events.html

Graphite
* https://answers.launchpad.net/graphite/+question/170491

Configurations
--------------
* Change memory allocated to memcached in supervisord.conf - default value is set to 256 MB

