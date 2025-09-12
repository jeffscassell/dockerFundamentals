FROM python:3.13-slim-trixie

WORKDIR /frontend
RUN pip install requests
COPY . .
CMD ["python3", "main.py"]