# Privilege Escalation Methodology

This section contains sanitized Windows and Linux privilege escalation methodology for authorized labs and assessments.

## Windows Review Areas

- User privileges and group membership
- Service permissions
- Scheduled tasks
- Stored credentials
- Unquoted service paths
- Weak file permissions
- Registry misconfigurations
- Local administrator exposure
- Credential material in scripts and configuration files

## Linux Review Areas

- SUID/SGID binaries
- Sudo rights
- Cron jobs
- Writable paths
- Service misconfigurations
- Kernel and package exposure
- Credential material in files
- Docker or container misconfigurations

## Reporting Focus

Privilege escalation findings should clearly explain:

- Starting privilege level
- Misconfiguration identified
- Potential impact
- Business risk
- Remediation steps
