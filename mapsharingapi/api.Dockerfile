
# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . .

# Expose the port that the Django API will run on
EXPOSE 8000

# Apply migrations and start the Django API server
CMD ["python3", "manage.py", "migrate"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "mapsharingapi.wsgi"]
