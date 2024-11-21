FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04
#FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# Set timezone
RUN ln --symbolic --force /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# Set locales
ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8"

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential vim \
    sudo wget curl git zip unzip gcc make cmake openssl openssh-client \
    libssl-dev libbz2-dev libreadline-dev \
    libsqlite3-dev python3-tk tk-dev python-tk \
    libfreetype6-dev libffi-dev liblzma-dev libsndfile1 ffmpeg zstd

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

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    echo '. $HOME/.cargo/env' >> $HOME/.bashrc




