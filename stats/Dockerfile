FROM python:3.14
RUN apt-get update

RUN pip install uv
COPY stats ./stats
COPY data ./data
WORKDIR /stats
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache -r pyproject.toml

# main project
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]