# Use the official Python image
FROM python:3.8-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    ca-certificates \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libgconf-2-4 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libx11-xcb1 \
    libxtst6 \
    libxrandr2 \
    xdg-utils \
    wget \
    libasound2 \
    libvulkan1 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y

# Install Python dependencies (including webdriver-manager)
RUN pip install selenium webdriver-manager

# Set display for headless operation
ENV DISPLAY=:99

# Copy the scraping script
COPY scrape.py /app/scrape.py

# Set the working directory
WORKDIR /app

# Run the scraping script
CMD ["python", "scrape.py"]
