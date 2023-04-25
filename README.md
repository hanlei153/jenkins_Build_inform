# jenkins_Build_inform
pipeline触发构建消息通知

### 克隆存储库
    git clone https://github.com/hanlei153/jenkins_Build_inform.git
### 启动
    cd jenkins_Build_inform
    python3 inform.py

### 容器运行，容器默认运行在8080端口
    cd jenkins_Build_inform
    docker build -t image:tag .
    docker run -it --name name image:tag
### 配置config.ini文件中的机器人地址，然后重启容器
    docker restart container_name
