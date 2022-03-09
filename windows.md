# windows: python, git, virtualenv
Do not use Microsoft Store Python (you might see permission problems when using PIP); instead get the 2 installers:

* Python https://www.python.org/downloads/
* git for windows https://gitforwindows.org/

Install the latter with 'Git Bash' added to your right mouseclick context menu, in any explorer folder.

## clone and initialize this repo
Open "Git Bash" (e.g. via start button, or right mouseclick "Git Bash Here" in e.g. folder D:\Code), then:

```
cd D:\Code
git clone https://github.com/drandreaskrueger/plutoalert drandreaskrueger_plutoalert
cd drandreaskrueger_plutoalert/
pip --version; python --version
pip install --upgrade pip virtualenv
python -m virtualenv venv
source ./venv/Scripts/activate
pip install -r requirements-minimum.txt
```

## run
the virtualenv must be activated before (otherwise python-import-packages are missing):

```
source ./venv/Scripts/activate
python -m plutoalert StarTrek
```

for more infos see the main [README.md](README.md).
