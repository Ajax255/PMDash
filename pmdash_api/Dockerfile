FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 5050

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]