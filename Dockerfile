FROM python:3
MAINTAINER Gregg Dixon "gregg.dixon@dxc.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
