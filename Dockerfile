# 1. Use a tiny version of Linux that already has Python
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our local script into the container's /app folder
COPY monitor.py .

# 4. Install the 'requests' library inside the container
RUN pip install requests

# 5. Tell the container what command to run when it starts
CMD ["python", "./monitor.py"]
