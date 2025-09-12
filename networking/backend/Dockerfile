FROM python:3.13-slim-trixie

WORKDIR /backend
RUN pip install flask
ENV FLASK_APP=main.py
COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]