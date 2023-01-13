FROM python:3.9.16-slim-bullseye
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt
COPY . /app
WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]