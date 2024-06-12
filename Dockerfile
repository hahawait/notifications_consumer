FROM python:3.12-alpine

RUN mkdir /src

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /src

CMD ["python", "src/main.py"]