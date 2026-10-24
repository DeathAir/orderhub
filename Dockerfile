FROM ubuntu:latest
LABEL authors="malor"

ENTRYPOINT ["top", "-b"]