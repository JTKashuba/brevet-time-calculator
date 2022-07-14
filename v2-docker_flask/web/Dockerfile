FROM python:2.7
MAINTAINER JT Kashuba "kashuba.jt@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

#RUN python app.py

ENTRYPOINT ["python"]
CMD ["app.py"]
