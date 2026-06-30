# Active Directory Security Assessment Methodology

This section documents a sanitized methodology for assessing Active Directory environments during authorized internal penetration tests and lab simulations.

## Objectives

- Identify privilege escalation paths.
- Assess domain password and account hygiene.
- Evaluate Kerberos-related risks.
- Review excessive privileges and misconfigured groups.
- Identify lateral movement opportunities.
- Document business impact and remediation guidance.

## Methodology

### 1. Initial Enumeration

- Identify domain controllers, domain trusts, DNS records, subnets, shares, and exposed services.
- Enumerate users, groups, computers, service accounts, and privileged objects.
- Review domain password policy and lockout settings.

### 2. Active Directory Graph Analysis

- Collect domain relationship data using approved tooling.
- Analyze attack paths to privileged groups.
- Review group nesting, ACL abuse paths, session data, local admin exposure, and misconfigured delegation.

### 3. Credential Exposure Review

- Assess common credential risks such as weak service account passwords, Kerberoasting exposure, AS-REP roasting exposure, password reuse, plaintext credentials, and overly permissive shares.

### 4. Lateral Movement Analysis

- Identify administrative access paths and protocol exposure.
- Review SMB, WinRM, RDP, LDAP, Kerberos, and RPC exposure.
- Validate findings only within the agreed rules of engagement.

### 5. Reporting

- Provide executive summary, technical findings, evidence, impact, likelihood, and remediation steps.
- Prioritize findings based on exploitability and business risk.

## Representative Finding Types

- Kerberoastable service accounts
- Weak domain password policy
- Excessive privileged group membership
- SMB signing not required
- LLMNR/NBT-NS enabled
- Inactive enabled accounts
- Non-expiring passwords
- Weak local administrator controls
- Unmanaged IPv6 exposure

## Safety Note

This content is intended for authorized assessment methodology and professional documentation only.
