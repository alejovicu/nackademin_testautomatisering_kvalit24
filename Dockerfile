FROM jenkins/jenkins:lts-jdk17

USER root
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pytest --break-system-packages

USER jenkins
