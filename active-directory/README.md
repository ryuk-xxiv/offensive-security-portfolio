# Active Directory Security Assessment Methodology

## Overview

Active Directory is the primary identity platform for most enterprise Windows environments and is frequently the primary objective during internal penetration tests. This methodology outlines the approach I use during authorized Active Directory security assessments to identify attack paths, privilege escalation opportunities, credential exposure, and weaknesses that could allow an attacker to compromise the domain.

This methodology is based on concepts from PTES, NIST SP 800-115, and industry best practices while remaining adaptable to the specific rules of engagement for each assessment.

---

# Assessment Objectives

The primary objectives of an Active Directory assessment are to:

- Identify privilege escalation paths
- Evaluate credential security
- Assess Active Directory configuration and trust relationships
- Identify opportunities for lateral movement
- Validate exploitability of discovered weaknesses
- Determine business impact
- Provide prioritized remediation recommendations

---

# Assessment Methodology

## Phase 1 – Initial Enumeration

The engagement begins with passive and authenticated enumeration to establish a complete understanding of the Active Directory environment.

Activities include:

- Identifying Domain Controllers
- Enumerating forests and domains
- Discovering domain trusts
- Reviewing DNS records
- Identifying organizational units
- Enumerating users, groups, computers, and service accounts
- Reviewing domain password and account lockout policies
- Identifying privileged groups
- Enumerating network shares
- Reviewing exposed services

The objective is to understand the attack surface while minimizing operational impact.

---

## Phase 2 – Active Directory Relationship Analysis

Once sufficient domain information has been collected, relationship analysis is performed to identify privilege escalation opportunities.

This phase includes reviewing:

- Group nesting
- ACL relationships
- Delegation configurations
- Administrative sessions
- Local administrator rights
- Attack paths to Tier 0 assets
- Excessive permissions
- Trust relationships

Relationship analysis helps identify indirect attack paths that may not be immediately obvious through manual enumeration.

---

## Phase 3 – Credential Security Assessment

Credential security is evaluated to identify weaknesses that could enable privilege escalation or lateral movement.

Areas assessed include:

- Kerberoasting exposure
- AS-REP Roasting exposure
- Weak service account passwords
- Password reuse
- Cached credentials
- Plaintext credential exposure
- Insecure file shares
- Group Policy Preference credentials
- Local Administrator Password Solution (LAPS) deployment
- Password policy effectiveness

---

## Phase 4 – Lateral Movement Assessment

Potential lateral movement opportunities are evaluated following the established Rules of Engagement.

Areas reviewed include:

- SMB
- WinRM
- RDP
- LDAP
- Kerberos
- RPC
- Remote administration exposure
- Administrative shares
- Privileged session exposure

Findings are validated only when permitted by the assessment scope.

---

## Phase 5 – Risk Validation

All findings undergo manual validation whenever possible.

The objective is to distinguish between:

- Scanner-generated findings
- Confirmed exploitable vulnerabilities
- Configuration weaknesses
- False positives

Validated findings are prioritized according to exploitability and business impact rather than CVSS score alone.

---

## Phase 6 – Reporting

Each engagement concludes with a detailed report containing:

- Executive Summary
- Assessment Scope
- Attack Narrative
- Technical Findings
- Evidence
- Business Impact
- Risk Rating
- Remediation Recommendations

Recommendations prioritize practical improvements that reduce attack paths while minimizing operational disruption.

---

# Common Findings

Examples of issues commonly identified during Active Directory assessments include:

- Kerberoastable service accounts
- Weak password policies
- Excessive privileged group membership
- Passwords configured to never expire
- Service accounts with excessive privileges
- SMB signing not required
- LLMNR/NBT-NS enabled
- Inactive enabled accounts
- Local administrator password reuse
- Missing Microsoft LAPS
- Weak delegation configurations
- Unmanaged IPv6 exposure

---

# Methodology References

- PTES (Penetration Testing Execution Standard)
- NIST SP 800-115
- MITRE ATT&CK
- Microsoft Security Baselines
- CIS Benchmarks

---

# Disclaimer

This repository documents my professional methodology for authorized security assessments and lab environments. It intentionally excludes exploit code, client information, or techniques that would facilitate unauthorized access.
