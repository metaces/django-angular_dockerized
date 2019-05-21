FROM python:3

# Set enviroment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# install dependencies.
RUN pip install -r /requirements.txt

# Set work directory
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

EXPOSE 80
