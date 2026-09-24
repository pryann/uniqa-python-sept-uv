
# Python

## Extensions

- python
- ruff
- code runner
- material icon theme

## ## Settings

- format on save: on
- eol: \n
- code runner : clear previous output: on
- code runner: show execution message: off

## Virtual venv

- venv létrhozása: python -m venv venv
- venv aktiválása: \venv\Scripts\Activate
- ha aktiválásnál execution policy hibát dob, akkor adminként futtatni:
  - `Set-ExecutionPolicy -Scope "CurrentUser" -ExecutionPolicy "RemoteSigned"` VAGY
  - `Set-ExecutionPolicy -Scope "CurrentUser" -ExecutionPolicy "Bypass"` VAGY
  - használd a cmd-t: activate.bat és ne ma ps1 file amit futtatni kell
- a venv mappa legyen a .gitgnoreba:
  - .gitignore fájl a györérbe és bele kell írni: venv

## Függőség

- telepítése: `pip install pandas`
- függőségek fileba írása: `pip freeze > requirement.txt`
- Kolléga gépén még nincs  venv mappa nincsenek meg a függőségek:
- python -m venv venv
- \venv\Scripts\Activate
- pip install -r requirements.txt

## UV

[[docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/)]([docs.astral.sh/uv/getting-started/installation](https:/docs.astral.sh/uv/getting-started/installation/))

- `uv init -no-package PROJECTNAME`
- `code PROJECTNAME`
- `uv add PACKAGENAME` : automatikusan létrehozza a venv-et és telepít
