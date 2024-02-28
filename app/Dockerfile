FROM python:3.8-alpine
WORKDIR /app
RUN pip install flask
RUN pip install pytz
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["app.py"]