FROM python:3.11.14

WORKDIR /app

COPY . .     

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python", "app.py" ]