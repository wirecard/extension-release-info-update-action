FROM python:3.7

RUN pip install lastversion gitpython pyyml markdown bs4 html2markdown

COPY *.json /usr/bin/
COPY . /usr/bin/
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
