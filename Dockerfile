FROM quay.io/jupyter/base-notebook

WORKDIR /workspace

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
