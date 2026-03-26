# Remove the old file
Remove-Item SECURITY.md -Force

# Create new file and add clean content
@"
# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the synology-api project, please report it responsibly. **Do not** create a public GitHub issue for security vulnerabilities.

### How to Report

Please email your findings to the project maintainers with the following information:

1. **Description**: A clear description of the vulnerability
2. **Location**: The specific file(s) and line(s) affected
3. **Severity**: Your assessment of the severity (Low, Medium, High, Critical)
4. **Proof of Concept**: Steps to reproduce or a code example demonstrating the vulnerability
5. **Impact**: Explain the potential impact of this vulnerability
6. **Suggested Fix**: If you have a fix in mind, please include it

### Response Timeline

- **Initial Response**: Within 48 hours of report submission
- **Assessment**: We will investigate and assess the vulnerability
- **Fix & Release**: We aim to release a fix within 30 days of confirmation
- **Disclosure**: Once a fix is released, we will credit you (unless you prefer anonymity)

---

## Security Best Practices

### For Users of synology-api

1. **Keep Dependencies Updated**
   - Regularly update the ``synology-api`` package: ``pip install --upgrade synology-api``
   - Keep your Python version and dependencies current

2. **Credential Management**
   - **Never hardcode credentials** in your code
   - Use environment variables or secure configuration files
   - Restrict file permissions on configuration files containing credentials
   - Example:
     ``````python
     import os
     from synology_api.filestation import FileStation
     
     fs = FileStation(
         ip=os.getenv('SYNOLOGY_IP'),
         port=os.getenv('SYNOLOGY_PORT'),
         username=os.getenv('SYNOLOGY_USER'),
         password=os.getenv('SYNOLOGY_PASS')
     )
     ``````

3. **HTTPS Only**
   - Always use HTTPS connections when communicating with Synology NAS
   - Verify SSL certificates in production environments

4. **Minimal Permissions**
   - Create dedicated service accounts with minimal required permissions
   - Don't use admin accounts for routine operations
   - Regularly audit account permissions

5. **Network Security**
   - Keep your Synology NAS on a secure network
   - Use VPN or SSH tunneling for remote access
   - Avoid exposing the NAS directly to the internet

---

## Known Issues & Limitations

### Authentication

- The library passes credentials over HTTPS. Ensure your connection is secure.
- Credentials are not encrypted in memory once loaded. Be mindful when debugging or logging.

### API Access

- Some Synology API endpoints may have rate limiting. Monitor for 429 responses.
- Certain operations may require specific user permissions on the NAS.

---

## Security Advisories

All security advisories and patches will be:
- Announced via GitHub Security Advisories
- Included in the CHANGELOG with security notes
- Tagged with ``[SECURITY]`` in release notes

Subscribe to repository notifications to stay informed of security updates.

---

## Scope

This security policy applies to:
- The ``synology-api`` Python package
- Code in the main repository
- Official releases on PyPI

### Out of Scope

- Third-party packages and dependencies (report to their respective maintainers)
- Synology NAS vulnerabilities (report to Synology directly)
- User configuration or deployment issues

---

## Contributing Secure Code

When contributing code to synology-api:

1. **Avoid Hardcoding Secrets**
   - Never commit credentials, tokens, or API keys
   - Use parameterized inputs or environment variables

2. **Input Validation**
   - Validate and sanitize user inputs
   - Avoid command injection vulnerabilities

3. **Dependency Review**
   - Keep dependencies minimal
   - Review new dependencies for security issues

4. **Follow Best Practices**
   - Use parameterized queries/API calls
   - Handle exceptions gracefully without leaking sensitive information
   - Follow NumPy docstring standards for clarity

---

## Thank You

Thank you for helping keep the synology-api project secure! We appreciate the security research community's responsible disclosure practices.

For questions or concerns about this policy, please open a discussion in the repository or contact the maintainers.
