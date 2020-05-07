FROM python:3

RUN pip install lastversion gitpython pyyml

COPY *.json /usr/bin/
COPY . /usr/bin/
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
