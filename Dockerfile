FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["flask", "--app=application.py", "run", "--host=0.0.0.0", "--port=8080"]