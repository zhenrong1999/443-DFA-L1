FROM python:3

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install graphviz graphviz-dev -y
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./99 main.py" ]