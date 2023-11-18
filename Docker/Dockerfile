# Basic configuration
FROM python:3.11-slim
COPY . . 

# Les mises à jour
RUN apt-get update &&\
    apt-get install -y gcc python3-dev &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt

# adding user 
RUN adduser --home /notebooks pyscrap
USER pyscrap 

# adding volumes
VOLUME /notebooks
WORKDIR /notebooks

CMD ["python", "main.py"]

