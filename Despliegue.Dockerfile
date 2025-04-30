From : python3.12-slim
Workdir /app
Copy requirements.txt .
Run pip install --no-cache-dir -r requirements.txt
Copy . .
CMD ["python", "ETL.py"]