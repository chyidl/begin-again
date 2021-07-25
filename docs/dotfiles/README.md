

* Oh My Zsh Plugins For Productive Developers
```
1. Zsh Autosuggestions
> suggested completion
    $ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    Add the plugin to the list of plugins for Oh My Zsh to load (inside ~/.zshrc)
plugins=(
    # other plugins...
    zsh-autosuggestions
        )

2. Sudo
> the sudo plugin takes what you just typed and adds a sudo at the beginning for

By pressing the esc key twice, you will have the same command with sudo prefixed without typing

3. Web Search
> adds aliases for searching with Google, Wiki

4. Copydir
> Copies the path of your current folder to the system clipboard.

5. Copyfile
> Puts the contents of a file in your system clipboard so you can paste it anywhere.

6. Copybuffer
> allows you to copy the text currently typed in the command line.

7. Json Tools
> Handy command line tools for dealing with json data.
    pp_json: pretty prints json
    is_json: return true if valid json; false otherwise
    urlencode_json: returns a url encoded string for the given hson
    urldecode_json: returns decoded json for the given url encoded string
```
