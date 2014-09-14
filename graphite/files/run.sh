#!/usr/bin/env bash

service supervisor start

num_retries=0
while true; do
    sleep 5
    process_state_postgres=$(service postgresql status | cut -d' ' -f4)
    if [[ ${process_state_postgres} == 'online' ]]; then
        supervisorctl start uwsgi
        supervisorctl start nginx
        exit 0
    fi
    
    if [[ ${num_retries} -eq 5 ]]; then
        exit 1
    fi
    num_retries=$((num_retries + 1))
done

