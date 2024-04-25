FROM ubuntu
RUN apt-get update && apt-get -y install python3 python3-pip
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
COPY app.py /opt/app.py
ENTRYPOINT FLASK_APP=/opt/src/app.py flask run --host=0.0.0.0 --port=8080
