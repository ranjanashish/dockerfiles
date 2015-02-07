dockerfiles
===========

Base Image - `debian:jessie <https://registry.hub.docker.com/_/debian/>`_

Docker Images
-------------
The docker images corresponding to each Dockerfile in this repository have already been built and can be downloaded from `docker hub <https://registry.hub.docker.com/repos/ranjanashish/>`_. However, if you want to build an image locally, navigate to directory of the Dockerfile and execute ``make``.

Fig
---
It is highly recommended to use `fig <http://www.fig.sh/>`_ for orchestration of the docker images.

List of Dockerfiles
-------------------
* `elasticsearch <https://github.com/ranjanashish/dockerfiles/blob/master/lib/dockerfiles/elasticsearch/Dockerfile>`_
* `memcached <https://github.com/ranjanashish/dockerfiles/blob/master/lib/dockerfiles/memcached/Dockerfile>`_
* `graphite-carbon <https://github.com/ranjanashish/dockerfiles/blob/master/lib/dockerfiles/graphite-carbon/Dockerfile>`_
* `graphite-web <https://github.com/ranjanashish/dockerfiles/blob/master/lib/dockerfiles/graphite-web/Dockerfile>`_
* `grafana <https://github.com/ranjanashish/dockerfiles/blob/master/lib/dockerfiles/grafana/Dockerfile>`_

List of fig scripts
-------------------
* `graphite <https://github.com/ranjanashish/dockerfiles/blob/master/fig-scripts/graphite/fig.yml>`_

Getting started (Debian-based distros)
--------------------------------------
1. Install docker:
   ``$ sudo apt-get install docker.io``
2. Add yourself to docker group (you will need to log-out and then log-in again for this to take effect; restart is not required):
   ``$ sudo usermod -a -G docker $USER``
3. Install fig:
   ``$ sudo apt-get install fig``
4. Clone the repository:
   ``$ git clone https://github.com/ranjanashish/dockerfiles ~/dockerfiles``

Graphite stack setup
--------------------
1. Navigate to fig-scripts directory of graphite
   ``$ cd ~/dockerfiles/fig-scripts/graphite``
2. Run fig
   ``$ fig up -d``

