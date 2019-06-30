FROM ubuntu:16.04


##安装配置java
ADD jdk-8u144-linux-x64.tar.gz /usr/local

###设置java 相关的环境变量
ENV JAVA_HOME /usr/local/jdk1.8.0_144
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH .:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
ENV PATH $PATH:$JAVA_HOME/bin:$JRE_HOME/bin


##安装配置python3.6
RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.6 python3.6-dev python3-pip

RUN ln -sfn /usr/bin/python3.6 /usr/bin/python3 && ln -sfn /usr/bin/python3 /usr/bin/python && ln -sfn /usr/bin/pip3 /usr/bin/pip

###更新python-packages
RUN python3.6 -m pip install --no-cache-dir -U pip
RUN python3.6 -m pip install --no-cache-dir -U setuptools

RUN python3.6 -m pip install numpy scipy pandas cloudpickle scikit-learn matplotlib Cython pyhanlp jieba sanic
RUN python3.6 -m pip install future protobuf enum34 pyyaml pyyaml typing rasa
 ##torch torchvision torchtext
RUN export LC_ALL=C.UTF-8

RUN hanlp