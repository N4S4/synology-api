# Contributing to synology-api

First things first many thanks for contributing!
I know it is not easy to spend free time to contribute to a passion!

the VERY little guideline written in here would be just the basis on how to contribute to this package.
As I say the following are just "guidelines" so do not feel obligated.

## Just behave

Have a look on our Code of conduct!

## How setup your environment

If you want to contribute to this package, you may want to setup your environment.

#### Install dependencies for your OS:
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

#### Windows setup

`asdf` does not have a native Windows installer, but it works on Windows
through **WSL2**, **Git Bash**, or **PowerShell Core**.
If you prefer not to use `asdf`, install the required tools
using one of the following package managers:

- [Chocolatey](https://chocolatey.org/install) (`choco`)
- [winget](https://github.com/microsoft/winget-cli) (built into Windows 10+)
- [Scoop](https://scoop.sh/)
- Manual installation from each tool's website

##### Required tools and versions

| Tool | Version | winget | choco | scoop |
|------|---------|--------|-------|-------|
| Node.js | `18.18.0` | `winget install OpenJS.NodeJS.LTS` | `choco install nodejs` | `scoop install nodejs-lts` |
| Python | `3.13.5` | manual install | `choco install python` | `scoop install python`¹ |
| Task (go-task) | `3.44.0` | `winget install Task.Task` | `choco install go-task` | `scoop install task` |
| shfmt | `3.11.0` | `winget install mvdan.shfmt` | `choco install shfmt` | `scoop install shfmt` |
| shellcheck | `0.10.0` | — | `choco install shellcheck` | `scoop install shellcheck` |
| pre-commit | `4.2.0` | — | — | `pip install pre-commit==4.2.0` |

¹ For Python 3.13 specifically: `scoop bucket add versions && scoop install python313`

> **About versions:** The `.tool-versions` file pins exact versions for `asdf`,
> but on Windows without `asdf`, installing the latest compatible version of
> each tool is sufficient. `choco` and `scoop` install the latest available
> version by default. To check available versions on Chocolatey:
> `choco list <package> --all-versions`.

You can also install **pre-commit** and **Task** via `pip`:

```bash
pip install pre-commit==4.2.0
pip install go-task-bin  # or: go install github.com/go-task/task/v3/cmd/task@latest
```

> **Note:** `numpydoc` validation (used by pre-commit hooks) may have parsing
> issues on Windows due to path separator differences. If you encounter
> problems, try running the validation inside **WSL** (Windows Subsystem for Linux)
> or in a Git Bash shell.

#### Windows PowerShell helpers

If you use PowerShell, you can add these helpers for common tasks:

```powershell
# Run pre-commit hooks
function Invoke-PreCommit { pre-commit run --all-files }

# Run numpydoc validation
function Invoke-Numpydoc { task numpydoc-validation }

# Install Python dependencies
function Install-PythonDeps { task install-python-deps }

# Format code
function Invoke-Format { task format }
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
We already have task for that, so you can run:
```bash
task venv
```


## Formating code

In task file is defined a task to format the code, you can run it with:
```bash
task format
```
Currently task will run `shellcheck` and `shfmt` on shell scripts. In near future it will run formatters on python files.


#### pre-commit hooks

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

## Validation

To ensure your code is valid and follows the project's standards, we use `numpydoc` for validation of docstrings.

To validate your code, you can run:
```bash
task numpydoc-validation
```

Alternatively, before committing, pre-commit hooks will automatically run this validation for the files you commit.

## Documentation

All documentation pages on `https://n4s4.github.io/synology-api/` are
**generated automatically** from docstrings when you push to ``master``.
You do **not** need to run anything locally.

How it works:

1. Write a good docstring using the
   [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
   format (validated by pre-commit).

2. Push your branch and open a Pull Request.

3. Once merged into ``master``, the deploy workflow automatically:
   * runs ``python3 -m scripts.docs_parser -a -l`` to generate fresh
     Markdown from every docstring in the codebase,
   * builds the Docusaurus site with ``npm run build``,
   * publishes the result to GitHub Pages.

**Nothing else is required.** The "Supported APIs" listing and every
class detail page (like ``SurveillanceStation``, ``Docker``, etc.) are
all produced from the same source — your Python docstrings.

If you want to preview the docs locally before pushing:

.. code-block:: bash

    task docs

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
