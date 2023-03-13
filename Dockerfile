FROM python:3.6

WORKDIR /home/philips/Docker_hands-on/Docker
COPY requirements.txt .
ENV HTTPS_PROXY http://185.46.212.97:9480
ENV HTTP_PROXY http://185.46.212.97:9480
RUN pip install -r requirements.txt
COPY settings.py .
COPY main.py .
COPY patient.py .
COPY api.py .
COPY testing.py .
COPY GUI.py .

CMD ["python", "./main.py"]
CMD ["python", "./settings.py"]
CMD ["python", "./patient.py"]
CMD ["python", "./api.py"]
CMD ["python", "./testing.py"]
CMD ["python", "./GUI.py"]
