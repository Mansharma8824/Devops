# Use the latest Python image
FROM python:latest
# Set the working directory
WORKDIR /Api-app

# Copy the Python script into the container
COPY . .
# Install the required packages
RUN pip install requests
RUN ls -la
# Command to run the application
CMD ["python", "ask_name_docker.py"]