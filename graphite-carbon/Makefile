.PHONY: default
default: build

.PHONY: all
all: build

.PHONY: build
build:
	docker build --no-cache=true --rm=true --tag ranjanashish/graphite-carbon .

.PHONY: clean
clean:
	docker rmi ranjanashish/graphite-carbon
