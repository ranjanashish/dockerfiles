TAG := ranjanashish/grafana

.PHONY: default
default: build

.PHONY: all
all: build

.PHONY: build
build:
	docker build --no-cache=true --rm=true --tag $(TAG) .

.PHONY: build_local
build_local:
	docker build --no-cache=false --rm=true --tag $(TAG) .

.PHONY: clean
clean:
	docker rmi $(TAG)
