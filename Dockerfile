FROM ubuntu
RUN apt-get update && apt-get -y install python3 python3-pip
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD FLASK_APP=/code/app.py flask run 
