FROM ghcr.io/dbt-labs/dbt-core:1.9.latest

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --requirement requirements.txt

