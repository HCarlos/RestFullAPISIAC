#!/usr/bin/env bash
git remote set-url origin https://github.com/HCarlos/SASOficialia.git
git remote add origin https://github.com/HCarlos/SASOficialia.git
# git remote set-url upstream https://github.com/HCarlos/SASOficialia.git

#   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

git config --global user.email "r0@tecnointel.mx"
git config --global user.name "HCarlos"
git config --global color.ui true
git config core.fileMode false
git config --global push.default simple

git branch main
git checkout main

git status

#git rm --cached /.env
git rm -r --cached .csv
git rm -r --cached sasoficial/settings.py
git rm -r --cached settings.py
git rm -r --cached sasoficial/configs/settings_production.py
git rm -r --cached settings_production.py
git rm -r --cached sasoficial/configs/

git rm -r --cached proyecto/__pycache__/
git rm -r --cached proyecto/migrations/__pycache__/
git rm -r --cached proyecto/modelform/__pycache__/
git rm -r --cached proyecto/reportes/__pycache__/
git rm -r --cached proyecto/ajax/__pycache__/

git rm -r --cached home/__pycache__/
git rm -r --cached home/migrations/__pycache__/

git rm -r --cached sasoficial/otros
git rm -r --cached sasoficial/otros/

git rm -r --cached sasoficial/__pycache__/
git rm -r --cached public/csv
git rm -r --cached public/csv/
git rm -r --cached .env
git rm -r --cached .env.example
git rm -r --cached .gitignore
git rm -r --cached .gitattributes
git rm -r --cached ./.editorconfig
git rm -r --cached ./.buildconfig
git rm --cached *.sh
git rm --cached report.pdf
git rm --cached *.pdf
git rm -r --cached .idea
git rm -r --cached otros
git rm -r --cached db.sqlite3

#git rm -r --cached composer.json
#git rm -r --cached composer.lock

git add .

git commit -m "SASOficialia - V-1-0-18 | PDJ4.0 Beta"

git push -u origin main --force

exit

