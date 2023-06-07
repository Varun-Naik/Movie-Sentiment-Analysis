# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . .

EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["app.py" ]