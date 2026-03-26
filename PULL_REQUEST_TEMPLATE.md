<!--
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

> If your changes include UI changes, API responses, or other visual elements,
> please attach screenshots or GIFs.

---

Thank you for contributing! 🙏