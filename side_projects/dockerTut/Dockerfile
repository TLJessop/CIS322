FROM python:2.7
MAINTAINER Thomas J "tjessop2@uoregon.edu"
RUN apt-get update -y
RUN apt-get install -y  python-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["hellp_world.py"]
