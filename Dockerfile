FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install scikit-learn
RUN pip install pandas
COPY rssi.csv /app/rssi.csv
COPY beacon_pos.csv /app/beacon_pos.csv
COPY app.py /app
EXPOSE 5000
CMD ["python", "app.py"]
