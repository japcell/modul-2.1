#!/bin/bash

#cd linuxopg
git add *
git config --global user.email "andsor41@gmail.com"
git config --global user.name "japcell"
echo Navn til commiten?
read commit
git commit -m $commit
git push
