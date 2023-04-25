FROM python:3.9-alpine3.17
MAINTAINER HANLEI
WORKDIR /opt
COPY . /opt/jenkins_Build_inform
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    cd /opt/jenkins_Build_inform && pip3 install flask
CMD ["sh", "-c", "cd /opt/jenkins_Build_inform && python3 inform.py"]