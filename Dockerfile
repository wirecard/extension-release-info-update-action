FROM python:3

RUN pip install lastversion gitpython pyyml markdown bs4

COPY *.json /usr/bin/
COPY . /usr/bin/
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
