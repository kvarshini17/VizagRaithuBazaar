# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set default port
ENV PORT 5000

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Initialize local sqlite database (if not using external DB)
# Note: In production you might want to run this manually or outside the build step,
# but adding it here ensures demo data is available when deployed instantly.
RUN python init_db_UPDATE.py || true
RUN python init_realistic_data.py || true
RUN python add_default_crops.py || true

# Expose the port the app runs on
EXPOSE ${PORT}

# Run gunicorn server
CMD gunicorn --bind 0.0.0.0:${PORT} app:app
