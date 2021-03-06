# Container image that runs your code
FROM python:3.9.10-alpine3.15

RUN pip install nbconvert
# Copies your code file from your action repository to the filesystem path `/` of the container
# COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
# COPY entrypoint.sh /entrypoint.sh
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python", "/main.py"]
# CMD [ "python", "main.py"]
