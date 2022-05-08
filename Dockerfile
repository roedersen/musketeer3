FROM python:3.8.1-slim

EXPOSE 8033

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn","--host", "0.0.0.0", "--port", "8033", "src.main:app" ]