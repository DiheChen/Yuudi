:: 許して、私は、本当にこれをするのが好きです
@echo off
git checkout --orphan  new_branch
git add -A
git commit -am "もう一度、清空 commit"
git branch -D master
git branch -m master
git push -f origin master
pause