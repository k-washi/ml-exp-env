FROM nvidia/cuda:11.1.1-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y build-essential vim \
    wget curl git zip gcc make openssl \
    libssl-dev libbz2-dev libreadline-dev \
    libsqlite3-dev python3-tk tk-dev python-tk \
    libfreetype6-dev libffi-dev liblzma-dev -y
RUN git clone https://github.com/yyuu/pyenv.git /root/.pyenv
ENV HOME  /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv --version
RUN pyenv install 3.8.6
RUN pyenv global 3.8.6
RUN python --version
RUN pyenv rehash
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install more-itertools jupyterlab japanize-matplotlib boto3

# JupyterNotebookのパスワード
RUN mkdir $HOME/.jupyter
COPY jupyter_notebook_config.py $HOME/.jupyter/
ENV PASSWORD password

WORKDIR /workspace