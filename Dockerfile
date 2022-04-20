FROM python:3.8
WORKDIR /app
COPY * .
RUN pip install -r requirements.txt
CMD pytest -v --html=pytest.html
EXPOSE 9000
CMD python -m http.server 9000




