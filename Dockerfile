FROM python:3.10

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]


# to run the build the dockerfile
# docker build -t flask-app .
# to run the container
# docker run -p 5000:5000 flask-app

# to create the docker volume and run
