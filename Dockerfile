FROM jenkins/jenkins:lts

USER root


COPY requirements.txt /tmp/requirements.txt

# Instalacja pakietów z requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Instalacja Playwright (jeśli nie jest uwzględniony w requirements.txt)
RUN pip3 install pytest-playwright && \
    playwright install

# Zmiana użytkownika z powrotem na jenkins

USER jenkins
