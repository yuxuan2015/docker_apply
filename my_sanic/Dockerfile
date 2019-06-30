FROM pyhanlp

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN export LC_ALL=C.UTF-8

#EXPOSE 8000

#CMD gunicorn app:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker
CMD ["python", "/app/app.py"]
