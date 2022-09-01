FROM python:3.10-alpine
WORKDIR /bot_src

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk --update add
RUN apk add libc-dev libffi-dev git bind-tools bash \ 
        && apk add --virtual build-deps gcc python3-dev musl-dev \
        && apk add --no-cache mariadb-dev
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
