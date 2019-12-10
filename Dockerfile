# THIS DOES NOT FUllY WORK YET

FROM python:3.8.0-slim-buster
RUN mkdir /app/
ADD finalgrades-linux.py /app
ADD requirements.txt /app
ADD config.py /app
RUN pip install -r /app/requirements.txt \
    && apt update \
    && apt install wget unzip chromium -y \
    && wget https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip \
    && unzip /chromedriver_linux64.zip -d /app/ \
    && rm /chromedriver_linux64.zip
CMD python /app/finalgrades-linux.py
