#!/bin/sh

git checkout main    # restore ourselves to main

# git config user.email "INSERT_EMAIL"
# git remote add upstream https://github.com/hjhornbeck/bayes_speedrun_cheating


git fetch upstream
git merge upstream/main main

jupyter-book build .
jupyter-book build --builder=pdflatex .

# pip3 install --user ghp-import
ghp-import -n -p -f _build/html

git checkout gh-pages
git add _build/latex/python.pdf
git commit -m "Auto-commit of LaTeX version."
git push --set-upstream origin gh-pages

git checkout main    # restore ourselves to main
git push             # as otherwise main keeps falling behind
