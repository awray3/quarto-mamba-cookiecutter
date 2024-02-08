#!/bin/bash

git init
dvc init
git add .

just create-env
just install-kernel