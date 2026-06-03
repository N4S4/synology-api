---
sidebar_position: 1
title: Contribution 101
---

# Contributing to synology-api

First things first — many thanks for contributing!
I know it is not easy to spend free time to contribute to a passion!

The **very** little guidelines written in here would be just the basis on how to contribute to this package.
As I say the following are just _guidelines_ so do not feel obligated, **except for the docs, please _follow_ the docs guidelines :)**

## 📝 Documentation

Documentation is **important**, specially in this end-user focused package, so please take a look at the [Documentation Guidelines](docs_guidelines).

## 😁 Be cool

Take a moment to check out our [Code of Conduct](conduct_code).

## 🛠️ Setup your environment

If you want to contribute to this package, you may want to setup your environment.

#### Install dependencies for your OS:
```bash
# macos
bash scripts/dependencies_darwin.sh

# linux
bash scripts/dependencies_linux.sh
```

Install the right version of tools:
```bash
asdf install
```

From now you can use Taskfile to run repetitive commands, for example:
```bash
task docs
```
To see all available tasks, run:
```bash
task --list
```

#### Install Python dependencies

To install Python dependencies, you can use the `task` command:
```bash
task install-python-deps
```
This will install all the required Python packages listed in `requirements.txt` and `requirements-dev.txt` using `pip` on your local machine.

#### Setup virtual environment

You can use `venv` to create a virtual environment for this project.
We already have a task for that, so you can run:
```bash
task venv
```

## 🔧 Code Formatting

In the Taskfile there is a task to format the code, you can run it with:
```bash
task format
```
Currently the task will run `shellcheck` and `shfmt` on shell scripts. In the near future it will run formatters on Python files.

#### Pre-commit hooks

To ensure your code is properly formatted and passes all checks, we use pre-commit hooks.
These hooks are installed automatically with the `task install` command (requires a Taskfile).
If you prefer, you can install them manually with:
```bash
pre-commit install
```

Hooks will run automatically before each commit, but you can also trigger them manually:
```bash
pre-commit run --all-files
# or
task pre-commit
```

These pre-commit hooks help keep the codebase clean and consistent by checking formatting, linting, and running tests.
They may seem strict at first, but they save time and reduce issues in the long run.

## ✅ Validation

To ensure your code is valid and follows the project's standards, we use `numpydoc` for validation of docstrings.

To validate your code, you can run:
```bash
task numpydoc-validation
```

Alternatively, before committing, pre-commit hooks will automatically run this validation for the files you commit.

## 🧪 Testing

You should **test your code** on your Synology NAS (_if you own one_).
This would save us plenty of time before merging any of your pull requests.
It does not mean that we will not test it before, but makes the process a lot easier and creates fewer open pull requests, which means less hassle and review.

## 🌐 Pull Request

Check if there is an active branch in progress and **always** make sure you are pulling into the right branch.

Before creating a **PR**:
- Use our [Pull Request Template](https://github.com/N4S4/synology-api/blob/master/.github/PULL_REQUEST_TEMPLATE.md) — it helps reviewers understand your changes quickly.
- Do not change setup, License and any other non-code related file. Changing them would only slow down the process with the consequent need of modifying the PR.

## 🫵 We want you

We need volunteers so you may be the **one**!

If you contribute we will become many which means, for me, this package will become even better.
Do not be scared or shy to make a pull request and/or let us know how we may improve this wrapper.
