FROM python:3.10-slim

# Install system dependencies if needed
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the app port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
