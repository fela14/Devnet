FROM ubuntu:18.04

LABEL maintainer="fela <k.fakeye@yahoo.com>"

# Update and install Python 3 and pip
RUN apt-get update -y && apt-get install -y python3-pip python3-dev

# Set working directory
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy your API source code
COPY ./API/api.py /app/

# Set entrypoint to run python3
ENTRYPOINT ["python3"]

# Default command to run your API script
CMD ["api.py"]
