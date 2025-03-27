#FROM ubuntu:latest
FROM python:3.12-slim-bookworm

# Expose port 5000 (adjust if your backend uses a different port)
EXPOSE 5000

# Set the time zone
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN apt-get update
#RUN apt-get install git python3 python3-pip python3-venv -y

# Set working directory for the backend
WORKDIR /backend

# Copy backend files
COPY backend/ .

# Copy requirements file (if you have one)
COPY requirements.txt .

# Create and activate a virtual environment
RUN python3 -m venv venv
RUN . venv/bin/activate

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the backend application (adjust the command as needed)
#this isn't working for some reason, starting in the yml file instead which is better anyway
#CMD ["python3", "main.py"] # or gunicorn, uvicorn, etc.
# Check if AUTO_START is set if not enter interactive mode
# For interactive mode
# . venv/bin/activate
# python3 main.py
#CMD ["/bin/bash", "-ic", "if [ -n \"$AUTO_START\" ]; then python3 main.py; else /bin/bash; fi"]