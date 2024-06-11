# Backend Dockerfile

# Use an appropriate base image
FROM python:3.9-slim

# Set environment variables
ENV DATABASE_URL=postgresql://postgres:1234@localhost:5432/snubh
ENV SECRET_KEY=supersecretkey
ENV DEBUG=true

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t toyproject-api .
# docker run -e DATABASE_URL=postgresql://postgres:1234@host.docker.internal:5432/snubh -p 8000:8000 toyproject-api