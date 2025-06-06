FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install flask pyyaml

EXPOSE 7655

CMD ["python", "web_admin/app.py"]
