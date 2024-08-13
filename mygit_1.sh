#!/usr/bin/env bash
git remote set-url origin https://github.com/HCarlos/RestFullAPISIAC.git
git remote add origin https://github.com/HCarlos/RestFullAPISIAC.git

# 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

# pwd : postg  =      R=D7,Z)$F%q,Kj?CP,DM{1CFNTtQ1B@4=V!d


git config --global user.email "r0@tecnointel.mx"
git config --global user.name "HCarlos"
git config --global color.ui true
git config core.fileMode false
git config --global push.default simple

git branch main
git checkout main

git status

git rm -r --cached .csv
git rm -r --cached RestFullAPI/settings.py
git rm -r --cached settings.py
git rm -r --cached RestFullAPI/configs/settings_production.py
git rm -r --cached settings_production.py
git rm -r --cached RestFullAPI/configs/


#git rm -r --cached home/__pycache__/
#git rm -r --cached home/migrations/__pycache__/

git rm -r --cached RestFullAPI/otros
git rm -r --cached RestFullAPI/otros/

git rm -r --cached RestFullAPI/__pycache__/
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

git commit -m "RestFullAPISIAC - V-1-0 | RestFullAPI-4.6 Beta"

git push -u origin main --force

exit

