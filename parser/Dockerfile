FROM python:3.14
RUN apt-get update

RUN pip install uv
WORKDIR /stats
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache -r pyproject.toml

# Copy only parser code + shared data
COPY parser ./parser
COPY data ./data