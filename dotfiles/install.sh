#!/bin/bash


BASEDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# vim
ln -s ${BASEDIR}/vimrc ~/.vimrc

# zsh
ln -s ${BASEDIR}/zshrc ~/.zshrc

# tmux
ln -s ${BASEDIR}/tmux.conf ~/.tmux.conf
ln -s ${BASEDIR}/tmux.conf.local ~/.tmux.conf.local

# git
ln -s ${BASEDIR}/gitconfig ~/.gitconfig

