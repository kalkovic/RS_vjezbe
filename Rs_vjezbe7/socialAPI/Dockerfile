FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 3500

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3500"]
