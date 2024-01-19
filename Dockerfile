FROM python:3.10

WORKDIR /workspace

COPY ./dist/*.whl /workspace

RUN pip install *.whl

CMD ["backend"]
