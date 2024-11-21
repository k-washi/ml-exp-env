#!/bin/bash

# Visual Studio Code :: Package list
pkglist=(
        charliermarsh.ruff
        codezombiech.gitignore
        eamodio.gitlens
        kevinrose.vsc-python-indent
        mosapride.zenkaku
        ms-azuretools.vscode-docker
        ms-pyright.pyright
        ms-python.python
        ms-vscode-remote.remote-containers
        njpwerner.autodocstring
        oderwat.indent-rainbow
        pkief.material-icon-theme
        shardulm94.trailing-spaces
        tamasfe.even-better-toml
        Gruntfuggly.todo-tree
        usernamehw.errorlens
        yzhang.markdown-all-in-one
        GitHub.copilot-labs
)

for var in ${pkglist[@]}
do
    code --install-extension $var
done
