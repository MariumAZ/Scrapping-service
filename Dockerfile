FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]