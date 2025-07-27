FROM python:3.11-slim
LABEL maintainer="ace"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8081
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]


# FROM python:3.13 AS builder
# WORKDIR /fapp
# COPY requirements.txt .
# RUN pip install --no-cache-dir --target=/fapp/deps -r requirements.txt
#
#
# FROM python:3.11-slim AS final
# WORKDIR /gapp
# COPY --from=builder /fapp /gapp
# COPY . .
# CMD ["uvicorn", "gapp:app"]
