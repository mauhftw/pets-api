FROM python:2.7
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
	python-pip && \
	pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
CMD flask run -h 0.0.0.0 -p 5000
#CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

