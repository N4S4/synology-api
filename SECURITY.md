# Security Policy for synology-api

The `synology-api` project provides Python wrappers for Synology DSM APIs.
We take security seriously and strive to keep the code safe, maintainable, and reliable.
This document explains how security issues are handled and provides guidance for reporting vulnerabilities.

---

## Scope

This security policy covers:

- Vulnerabilities in the Python wrapper code (`synology_api/`)
- Authentication and session handling mechanisms
- API interactions, including data validation and error handling
- Dependencies and third-party libraries used by this project
- Documentation and example scripts that may expose sensitive information

---

## Reporting a Vulnerability

We strongly encourage responsible disclosure. Do **not** post vulnerabilities in public issues or pull requests.

| Channel                      | How to report                                                                                                                               |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Email**                    | Send a private message to the maintainer: **renato@visaggio.io**. Include detailed steps to reproduce, affected DSM versions, and any logs. |
| **GitHub Security Advisory** | Use GitHubâ€™s *Security* tab if you are a GitHub user with a private repository.                                                             |
| **Encrypted Communication**  | For highly sensitive reports, use PGP encryption. Contact maintainer to obtain a public key.                                                |

Please include:

- DSM version(s) tested
- Synology API endpoint affected (e.g., `SYNO.FileStation.List`)
- Authentication method used (e.g., account password, API token)
- Minimal reproducible code sample or steps

We will acknowledge receipt within 48 hours.

---

## Responsible Disclosure Timeline

1. **Acknowledgment** â€“ We confirm receipt of the report within 48 hours.
2. **Investigation** â€“ The issue is verified, and its impact is assessed.
3. **Fix Development** â€“ A patch is created and tested, including:
    - API endpoint validation
    - Session handling and token security
    - Secure error handling
4. **Release & Notification** â€“ The patch is released, tagged on PyPI and GitHub, and affected users notified.
5. **Public Disclosure** â€“ After 30 days (or sooner if agreed), details may be disclosed publicly.

---

## Authentication & Session Security

- All authentication is handled through Synology DSM secure endpoints.
- Passwords or API tokens **must not** be stored in plaintext in code or documentation.
- Sessions are automatically refreshed and invalidated when expired.
- Contributors should follow best practices when handling credentials in tests or examples.

---

## Data Validation & API Security

- All user input sent to the DSM APIs is validated.
- Error handling ensures that invalid requests do not expose sensitive information.
- Avoid constructing requests that could trigger unintended API behavior (e.g., mass deletion).
- Contributors should maintain minimal privileges when testing APIs.

---

## TLS & Network Security

- All communication with Synology devices should use HTTPS endpoints.
- Self-signed certificates may be used in testing but should be properly validated in production.
- Avoid transmitting credentials over unsecured networks.

---

## Dependency & Package Security

- Dependencies are reviewed for security issues.
- Use pinned versions in `requirements.txt` or `requirements-dev.txt` to avoid unintentional upgrades.
- Regularly check for security advisories using tools like `safety` or `pip-audit`.

---

## Example: Reporting an API Security Issue

    from synology_api import filestation

    # Example demonstrating authentication and file listing
    # Do not include real credentials in public reports

    client = filestation.FileStation('192.168.1.100', 'admin', '*****')
    files = client.list('/home/user')

Include logs, error messages, and DSM version when reporting issues.

---

## Contact

- **Maintainer**: Renato Visaggio
- **Email**: [Synology Api Mail](mailto:synology.python.api@gmail.com)
- **GitHub**: [@N4S4](https://github.com/N4S4)

---

## Additional Security Resources

- **Python Secure Coding**: https://docs.python.org/3/howto/security.html
- **Synology DSM Security Best Practices**: https://www.synology.com/en-us/knowledgebase/DSM/security
- **Open Source Vulnerability Database**: https://ossindex.sonatype.org/

---

## License

This file is part of the `synology-api` project and is released under the MIT license.
Copyright Â© 2024â€“2026 Renato Visaggio.
