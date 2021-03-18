FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN useradd appuser && chown -R appuser /app
USER appuser
ENTRYPOINT ["python"]
CMD ["./ml_flask.py"]