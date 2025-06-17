#!/usr/bin/env bash
# script to install dependencies for asdf on Linux

# https://asdf-vm.com/guide/getting-started.html#plugin-dependencies
# https://asdf-vm.com/guide/getting-started.html#install-dependencies
echo "Installing dependencies for macOS..."
brew install coreutils git bash gpg gawk asdf

echo "Installing asdf..."
brew install asdf

echo "Installing asdf plugins..."
asdf plugin add nodejs
asdf plugin add python
asdf plugin add task