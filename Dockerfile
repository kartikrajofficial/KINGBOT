# KINGBOT - UserBot


FROM python:3.9.2-slim-buster
COPY resources/startup/deploy.sh .
RUN chmod +x deploy.sh && sh deploy.sh
WORKDIR /root/kartikrajofficial/
CMD ["bash", "resources/startup/startup.sh"]
