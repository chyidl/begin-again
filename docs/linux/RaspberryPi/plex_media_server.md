Plex Media Server
=================
> Plex is a streaming media server that lets you organize your video, music, and photo collections and stream your media to your computer, phone, tablet, or TV at any time and from anywhere.

* 1. Add the Plex APT repository to your system and import the repository GPG key:
```
  $ curl https://downloads.plex.tv/plex-keys/PlexSign.key | sudo apt-key add -
  $ echo deb https://downloads.plex.tv/repo/deb public main | sudo tee /etc/apt/sources.list.d/plexmediaserver.list
```

* 2. update the apt package list and install the latest server version
```
$ sudo apt update
$ sudo apt install plexmediaserver
```

* 3. To verify the Plex is running, check the service status
```
$ sudo systemctl status plexmediaserver
```
