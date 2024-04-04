FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# Set timezone
RUN ln --symbolic --force /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# Set locales
ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8"

RUN apt-get update -y && apt-get install -y build-essential vim \
    sudo wget curl git zip gcc make cmake openssl \
    libssl-dev libbz2-dev libreadline-dev \
    libsqlite3-dev python3-tk tk-dev python-tk \
    libfreetype6-dev libffi-dev liblzma-dev libsndfile1 ffmpeg zstd -y

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

ARG project_name=mlexpenv
ARG uid=1001
ARG gid=1001
ARG username=mluser
ARG APPLICATION_DIRECTORY=/home/${username}/${project_name}

RUN echo "uid ${uid}"
RUN echo "gid ${gid}"
RUN echo "username ${username}"
# RUN groupadd -r -f -g ${gid} ${username} && useradd -o -r -l -u ${uid} -g ${gid} -ms /bin/bash ${username}
RUN addgroup --gid ${gid} ${username} && \
    adduser --disabled-password --gecos '' --uid ${uid} --gid ${gid} ${username} && \
    usermod --append --groups sudo ${username} && \
    echo '%sudo ALL=(ALL:ALL) NOPASSWD:ALL' >> '/etc/sudoers'


USER ${username}
WORKDIR ${APPLICATION_DIRECTORY}

# python関連
RUN git clone https://github.com/yyuu/pyenv.git /home/${username}/.pyenv
ENV HOME /home/${username}
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN ls $PYENV_ROOT/bin
RUN pyenv --version

RUN pyenv install 3.10.11
RUN pyenv global 3.10.11

RUN python --version
RUN pyenv rehash
RUN pip install --upgrade pip setuptools requests
RUN pip install poetry==1.7.1




