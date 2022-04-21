FROM python:3.8
WORKDIR /app
COPY . /app
RUN mkdir -p /app/reports
ENV PYTHONPATH /app
RUN pip install -r requirements.txt
EXPOSE 7000
CMD pytest -v --gherkin-terminal-reporter --html=/app/reports/crypto_bdd.html \
    --junitxml=/app/reports/crypto_bdd_junit.xml ; \
    python -m http.server 7000 --directory /app/reports


