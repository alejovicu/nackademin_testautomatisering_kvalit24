FROM jenkins/jenkins:lts-jdk17

USER root

# Install Python3, pip, and dependencies for browsers
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-venv \
        python3-dev \
        build-essential \
        libssl-dev \
        libffi-dev \
        curl \
        git \
        libasound2 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdbus-1-3 \
        libdrm2 \
        libgbm1 \
        libglib2.0-0 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcomposite1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxkbcommon0 \
        libxrandr2 \
        libxcursor1 \
        libxrender1 \
        libxss1 \
        libxtst6 \
        libpango-1.0-0 \
        libcairo2 \
        libgdk-pixbuf-2.0-0 \
        fonts-liberation \
        libjpeg-turbo-progs \
        libwoff1 \
        xdg-utils && \
    rm -rf /var/lib/apt/lists/*


# Switch back to Jenkins user
USER jenkins

# Create a python venv in home for jenkins user and upgrade pip
RUN python3 -m venv /var/jenkins_home/.venv && \
    . /var/jenkins_home/.venv/bin/activate && \
    pip install --upgrade pip

# Install required Python packages
RUN . /var/jenkins_home/.venv/bin/activate && pip install \
        fastapi==0.116.1 \
        SQLAlchemy==2.0.43 \
        passlib==1.7.4 \
        uvicorn==0.35.0 \
        bcrypt==4.3.0 \
        python-jose==3.5.0 \
        python-multipart==0.0.20 \
        pytest-playwright==0.7.0 \
        requests==2.32.5 && \
    playwright install chromium && \
    playwright install firefox
