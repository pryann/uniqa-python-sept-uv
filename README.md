
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


## REST
- CRUD 
  - Create
    - POST
  - Read
    - GET
  - Update
    - PUT - replace
    - PATCH - partial update
  - Delete
- plural:
  - /posts, /users
    - PostService, PostRepo, PostController (API)
    - DB: Post/Posts
    - person - people???
    - billingAndress - billingAddresses
    - knife - knives
- /webinar/:webinarId/lessons/:lessonsId/presenters/predenterId
- CQRS...

- /posts?start_date=.....&end_date=...&search=....&lang=...&lang=...
- QUERY method (HELLL YEAH!!!)
- QUERY json-be 
- QUERY, POST
  - post/command/createPost
  - post/command/updatePostById
  - post/query/fetchAllPosts
  - post/query/findPostById