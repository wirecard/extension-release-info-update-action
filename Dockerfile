FROM python:3

RUN pip install lastversion gitpython pyyml markdown bs4 html2markdown

#copy config files to the same folder as scripts
COPY *.json /usr/bin/
COPY . /usr/bin/
COPY entrypoint.sh /entrypoint.sh
#TODO remove test_data


ENTRYPOINT ["/entrypoint.sh"]
