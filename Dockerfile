# Step 1: Use a lean Python base image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 4: Install system dependencies required by psycopg2
# This helps prevent potential build issues.
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Step 5: Copy and install Python dependencies
# This leverages Docker's layer caching. The dependencies are only re-installed
# if the requirements.txt file changes.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the application code into the container
COPY ./app /app/app

# Step 7: Expose the port the application will run on
EXPOSE 8000

# Step 8: Define the command to run the application
# Uvicorn is set to run on host 0.0.0.0 to be accessible from outside the container.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
