FROM pytorch/pytorch:2.6.0-cpu-py3.11-ubuntu22.04
RUN pip install uv

RUN apt update && \
    apt install -y espeak-ng && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . ./

RUN uv pip install --system -e . && uv pip install --system -e .[compile]
