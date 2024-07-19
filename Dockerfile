FROM jenkins/jenkins:lts

USER root


COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxkbcommon0 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Instalacja pakietów z requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Instalacja Playwright (jeśli nie jest uwzględniony w requirements.txt)
RUN pip3 install pytest-playwright && \
    playwright install

# Zmiana użytkownika z powrotem na jenkins

USER jenkins
