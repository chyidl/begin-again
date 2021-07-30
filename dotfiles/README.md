# Dotfiles

* Why would I want my dotfiles on Github?
    * Backup, restore, and sync the prefs and settings for your toolbox. Your dotfiles might be the most important files on your machine.
    * Learn from the community. Discover new tools for your toolbox and new tricks for the ones you already use.
    * Share what you've learned with the rest of us.

* Installation
```
There are two possible ways to install dotfiles in systems:
    copying
    symbolically linking files -

idempotent install script, a program that be run multiple time witout having any effect beyind the initial application.
```
[install shell script]()

* krew
> Krew is the package manager for kubectl plugins
> Krew helps you discover and install kubectl plugins on your machine.
```
# Run this command to download and install krew.
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/krew.tar.gz" &&
  tar zxvf krew.tar.gz &&
  KREW=./krew-"${OS}_${ARCH}" &&
  "$KREW" install krew
)

# Add the $HOME/.krew/bin directory to your PATH environment variable.
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"

# Run kubectl krew to check the installation
$ kubectl krew update
```

* kubectx + kubens: Power tools for kubectl
> Faster way to switch between clusters and namaspaces in kubectl
```
$ kubectl krew install ctx
$ kubectl krew install ns

After installing, the tools will be available as kubectl ctx and kubectl ns
```


### Appendix
* [dotfiles](https://dotfiles.github.io/)



