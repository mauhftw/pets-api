FROM python:2.7
WORKDIR /app
COPY . /app
RUN sudo apt-get update && sudo apt-get install -y \
	python-pip
RUN pip install -r requirements.txt
EXPOSE 5000

