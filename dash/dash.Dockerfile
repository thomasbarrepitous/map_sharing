# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Dash app files into the container
COPY . .

# Expose the port that the Dash app will run on
EXPOSE 8050

# Start the Dash application
CMD ["python3", "-u", "app.py"]


