# Use official Python image as base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Set environment variables for production
ENV DATABASE_URL=postgresql://postgres:WpKDmbEgsugFiIzfhnSZQyeXZksTbUra@postgres.railway.internal:5432/railway?sslmode=require

# Run migrations before starting the server
RUN python -m app.database

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

