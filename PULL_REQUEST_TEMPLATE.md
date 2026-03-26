<!--
<<<<<<< Updated upstream
  Pull Request Template for N4S4/synology-api
  ==========================================
  Fill in the fields below to describe your changes.  
  A thorough description helps reviewers understand your intent and makes the
  review process smoother.
-->

## Summary

**What does this pull request do?**  
A brief, one-sentence description of the changes.

---

## Motivation & Problem Statement

**Why is this PR needed?**  
Outline the problem being solved or the improvement being made.

**Related Issue(s)**  
Closes #<!-- issue number -->

---

## Implementation Details

**What changes were made?**
- List the files affected and the nature of changes (add, modify, delete)
- Mention any new tests added or existing tests updated
- List any new dependencies added to `requirements.txt` or `requirements-dev.txt`

---

## Documentation & Docstrings

- [ ] Updated docstrings using NumPy format (if code changes made)
- [ ] Ran `task numpydoc-validation` and all checks passed
- [ ] Added or updated documentation in `documentation/docs/` (if applicable)
- [ ] Ran `task docs-parser` to generate and validate documentation
- [ ] Ran `task docs-build` to verify documentation builds without errors

---

## Testing Checklist

- [ ] I have read and followed the [Contributing guidelines](CONTRIBUTING.md)
- [ ] All new or modified code is covered by unit tests (`tests/`)
- [ ] Tests pass locally: `pytest`
- [ ] Code formatting passes: `task format`
- [ ] Pre-commit hooks pass: `task pre-commit`
- [ ] NumPy docstring validation passes: `task numpydoc-validation`
- [ ] Documentation generation passes: `task docs-parser`
- [ ] Tested on actual Synology NAS (if applicable)

---

## Breaking Changes

- [ ] This PR contains breaking changes
- [ ] If yes, please document them below:

---

## Additional Notes

Anything else reviewers should know?
- Known limitations
- Required manual steps
- Performance implications
- Design decisions

---

## Screenshots / Media

If your changes include API responses, new features, or visual elements, please attach screenshots or GIFs.

---

## Pre-Submission Commands

Run these commands locally before opening the PR:
```bash
pip install -r requirements-dev.txt
task format
task pre-commit
task numpydoc-validation
task docs-parser
pytest
```
---

## Screenshots / Media
=======
Pull Request Template for N4S4/synology-api
Fill in the fields below to describe your changes.
A thorough description helps reviewers understand your intent and makes the
review process smoother.
-->

## :card_file_box: Summary

> **What does this pull request do?**
> A brief, one-sentence description.

---

## :rocket: Motivation & Problem Statement

> **Why is this PR needed?**
> Outline the problem being solved or the improvement being made.

---

## :wrench: Implementation Details

> **What changes were made?**
> - List the files affected and the nature of the changes (add, modify, delete).
> - Mention any new tests added or existing ones updated.
> - If it touches the documentation, indicate which sections were updated.

---

## :checkered_flag: Checklist

- [ ] I have read and followed the [Contributing guidelines](CONTRIBUTING.md).
- [ ] All new or modified code is covered by unit tests (`tests/`).
- [ ] Tests pass locally (`pytest`).
- [ ] I added or updated documentation where necessary.
- [ ] I updated the changelog or added a new section if this is a major change.
- [ ] I followed the style guidelines (`black`, `flake8`, etc.).
- [ ] I ran `pre-commit` and addressed any linting issues.

> **Note:** If you added a new API wrapper, please update `docs/` and add the
> corresponding entries to `APIs - Supported APIs` in the README.

---

## :memo: Related Issue

> **Issue number(s) this PR addresses**
> `#123`

---

## :hammer: Additional Notes

> Anything else that reviewers should know?
> - Known limitations
> - Required manual steps
> - Performance implications

---

## :sunglasses: Test & Build Status

> Run the following locally before opening the PR:

    pip install -r requirements-dev.txt
    pre-commit run --all-files
    pytest

---

## :eyes: Screenshots / Media
>>>>>>> Stashed changes

> If your changes include UI changes, API responses, or other visual elements,
> please attach screenshots or GIFs.

---

<<<<<<< Updated upstream
Thank you for contributing! 🙏
=======
Thank you for contributing! 🙏
>>>>>>> Stashed changes
