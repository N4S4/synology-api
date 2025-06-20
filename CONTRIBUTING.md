# Contributing to synology-api

First things first many thanks for contributing!
I know it is not easy to spend free time to contribute to a passion!

the VERY little guideline written in here would be just the basis on how to contribute to this package.
As I say the following are just "guidelines" so do not feel obligated.

## Just behave

Have a look on our Code of conduct!

## How setup your environment

If you want to contribute to this package, you may want to setup your environment.

Install dependencies for your OS:
```bash
# macos 
bash scripts/dependencies_darwin.sh

# linux
bash scripts/dependencies_linux.sh
```

Install right version of tools
```bash
asdf install 
```

From now you can use Taskfile to run repetitive commands, for example:
```bash
task docs
```

## Testing

We would appreciate if you test your code on your Synology NAS (if you own one),
this would save us plenty time before merging any of your pull request,
It does not mean that we will not test it before but makes process lot easier,
less open pull requests which means less hassle and review.

## Pull Request

Check if there is an active branch in progress and Always make sure you are pulling into the right branch.
Before creating a PR make sure to do not change setup, License and any other non code related file.
Changing them would only slow down the process with consequently need of modifying the PR

## We want you

We need volunteers so you may be the one!
If you contribute we will become many which means, for me, this package will become even better.
Do not be scared or shy to make a pull request and/or let us how we may improve this wrapper.
