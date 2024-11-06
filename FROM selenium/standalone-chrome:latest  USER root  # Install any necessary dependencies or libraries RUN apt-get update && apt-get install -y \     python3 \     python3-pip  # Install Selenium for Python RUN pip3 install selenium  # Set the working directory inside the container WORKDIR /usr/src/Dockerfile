FROM selenium/standalone-chrome:latest

USER root

# Install any necessary dependencies or libraries
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Install Selenium for Python
RUN pip3 install selenium

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy your scraping script into the container
COPY scrape.py .

CMD ["python3", "scrape.py"]
