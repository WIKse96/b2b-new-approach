FROM jenkins/jenkins:lts

USER root

# Aktualizacja pakietów i instalacja narzędzi
RUN apt-get update && \
    apt-get install -y python3-pip git

# Skopiowanie pliku requirements.txt do kontenera
COPY requirements.txt /tmp/requirements.txt

# Instalacja pakietów z requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Instalacja Playwright (jeśli nie jest uwzględniony w requirements.txt)
RUN pip3 install pytest-playwright && \
    playwright install

# Zmiana użytkownika z powrotem na jenkins
USER jenkins
