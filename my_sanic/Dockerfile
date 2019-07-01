FROM pyhanlp

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN export LC_ALL=C.UTF-8

#EXPOSE 8000

CMD ["python", "/app/app.py"]
