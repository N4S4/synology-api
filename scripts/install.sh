#!/usr/bin/env bash
# script to install same tools versions for this project

# install tools versions specified in .tool-versions file
asdf install

# install pre-commit hooks
pre-commit install --hook-type pre-commit --hook-type pre-push
