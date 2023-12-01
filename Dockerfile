FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Bangkok

COPY . .

RUN pip install -U pip
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

RUN python ./eval.py

ENTRYPOINT ["tail", "-f", "/dev/null"]
