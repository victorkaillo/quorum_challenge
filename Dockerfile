FROM python:3.11

# UPDATE APT-GET
RUN apt-get -y update

COPY . /app
COPY './requirements.txt' .
COPY './.env' .

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

ENV PORT=80
EXPOSE $PORT

# CMD ["python", "src/data_extract_service.py"]
# docker build -t quorumchallenge --platform linux/amd64 .
# docker run -it --entrypoint /bin/bash quorumchallenge -s