# Set base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Expose port (adjust if necessary)
EXPOSE 8000

# Run the Django application (use Gunicorn for production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "configs.wsgi:application"]
