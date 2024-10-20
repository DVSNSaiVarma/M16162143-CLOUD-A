# Use a smaller base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /home/data

# Copy the script and text files
COPY scripts.py /home/data/scripts.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip

# Command to run the script
CMD ["python", "scripts.py"]
