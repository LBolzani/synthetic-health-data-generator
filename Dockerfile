FROM python:3.7-slim

EXPOSE 8501

WORKDIR /synthetic-health-data-generator

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/LBolzani/synthetic-health-data-generator.git .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "/synthetic-health-data-generator/web-ui/src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]