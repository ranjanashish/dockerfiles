#!/usr/bin/env python
"""
Event listener for supervisor
"""

import os
import sys

def write_stdout(msg):
    """Write message to stdout

    Args:
        msg (str): message to print on stdout
    Returns:
        None
    """
    sys.stdout.write(msg)
    sys.stdout.flush()

def write_stderr(msg):
    """Write message to stderr

    Args:
        msg (str): message to print on stderr
    Returns:
        None
    """
    sys.stderr.write(msg)
    sys.stderr.flush()

def main():
    """main function
    """
    is_postgres_running = False
    is_memcached_running = False
    event_counter = 1

    while 1:
        # transition from ACKNOWLEDGED to READY state
        write_stdout('READY\n')

        write_stderr('Event: ' + str(event_counter) + '\n')

        # read event header
        event_header = sys.stdin.readline()
        write_stderr(event_header)
        headers = dict([x.split(':') for x in event_header.split()])

        # read event payload
        event_payload = sys.stdin.read(int(headers['len']))
        write_stderr(event_payload)
        events = [dict([y.split(':') for y in x.split()])
                  for x in event_payload.split('\n')]

        if headers['eventname'] == 'PROCESS_STATE_RUNNING':
            for event in events:
                if event['processname'] == 'postgres':
                    is_postgres_running = True
                elif event['processname'] == 'memcached':
                    is_memcached_running = True

        # start uwsgi and nginx if postgres and memcached are running
        if is_postgres_running and is_memcached_running:
            os.system('supervisorctl start uwsgi')
            os.system('supervisorctl start nginx')
            sys.exit(0)

        # transition from READY to ACKNOWLEDGED state
        write_stdout('RESULT 2\nOK')

        event_counter = event_counter + 1
        write_stderr('\n')

if __name__ == '__main__':
    main()

