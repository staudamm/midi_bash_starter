# midi_bash_starter

## 1. Clone github repository
```bazaar
git clone git@github.com:staudamm/midi_bash_starter.git
```
Then enter the root directory of the project: `cd midi_bash_starter`

## 2. Install dependecies
### 2.1 Python environment (pyenv) and required python version
```bazaar
brew update
brew install pyenv
```
Then make sure to follow these steps https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv. If you use the `zsh`-shell, the steps are
```bazaar
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
Once pyenv is installed and configured, you can use it to 
1. install the python version and 
2. use that version whenever you run a python command (see the README at https://github.com/pyenv/pyenv)
```bazaar
pyenv install 3.10.3
pyenv global 3.10.3
```

### 2.2 Install package requirements
Inside the root-folder of this project, run
```bazaar
pip install -r requirements.txt
```

## 3. Run the script
When you run `python midi_bach_starter.py` you are prompted to enter 
1. The midi-device to use
2. the midi-channel to listen to
3. the midi-note to listen to (numbered from 0 to 127)
4. the absolute path to the bash-script that you want to run (if you type enter, the script will call the file `default.sh` thats contained in the repo)

To end the script, type `CTRL+c`

To test the code, the repo also contains a dummy-script `sender.py`, that sends a `note_on` with the parameters specified in the top of the file (run it with `python sender.py`)  
