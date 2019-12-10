# THIS DOES NOT FUllY WORK YET

FROM 3.8.0-slim-buster
ADD finalgrades.py / \
    requirements.txt /
RUN pip install requirements.txt
