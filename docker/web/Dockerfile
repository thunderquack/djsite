FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
run ls
COPY requirements.txt /src/
RUN pip install -r requirements.txt
#COPY . /src/