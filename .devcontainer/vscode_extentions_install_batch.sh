#!/bin/bash
 
# Visual Studio Code :: Package list
pkglist=(
        ms-python.python
		donjayamanne.python-extension-pack
		oderwat.indent-rainbow
		pkief.material-icon-theme
		mosapride.zenkaku
		aaron-bond.better-comments
		shardulm94.trailing-spaces
		kevinrose.vsc-python-indent
		njpwerner.autodocstring
		ms-python.vscode-pylance
		gruntfuggly.todo-tree
		bungcip.better-toml
		GitHub.copilot
		GitHub.copilot-chat
)
 
for var in ${pkglist[@]}
do
    code --install-extension $var
done