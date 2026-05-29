# Alisha Chaudhary

### Cybersecurity Analyst · Detection Engineering · OSINT · Vulnerability Research

[![LinkedIn](https://img.shields.io/badge/LinkedIn-alisha--chaudhary-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alisha-chaudhary-/)
[![Location](https://img.shields.io/badge/Location-Hyderabad%2C%20India-informational?style=flat&logo=googlemaps&logoColor=white)](https://github.com/Alisha-chaudhary)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-alisha-212C42?style=flat&logo=tryhackme&logoColor=white)](https://tryhackme.com)

---

## About Me

## About Me

I work on the defensive side of security, focusing on detection engineering, threat intelligence, and vulnerability analysis. I approach security research with an emphasis on observation and evidence: build a controlled environment, test assumptions, and document what actually happens rather than what is expected.

That mindset shaped the SSH enumeration project. When the attack itself failed, the more valuable question became why it failed and what traces remained visible from a defender's perspective. The same approach influenced ThreatLens. Raw scan output alone provides limited value; meaningful insights come from correlation, context, and a risk score that reflects real-world relevance.

I've co-authored a peer-reviewed publication in AI/healthcare research, contributed to detection tooling, and I'm currently expanding my work in network security and applied cryptography. I enjoy building in public, documenting projects thoroughly, and exploring the difference between simply making something work and fully understanding "how" and "why it works".


---

## Projects

### [ssh-enum](https://github.com/Alisha-chaudhary/ssh-enum) · Python · Attack Analysis & Detection Engineering

A controlled investigation into SSH user enumeration on Ubuntu 22.04.5 LTS + OpenSSH 8.9p1. Started as an attack study and pivoted into detection engineering when the attack surface turned out to be smaller than expected.

**What it covers:**
- Parallel testing across Paramiko, Hydra, Metasploit, and custom banner fingerprinting
- Welch's t-test + Cohen's d on ~500 timing samples — no statistically significant side-channel found (p > 0.40, Δ ≈ 1ms)
- Four log-based detection patterns: rapid user probes, wordlist correlation, sequential timing (CoV), distributed probing
- Full Python codebase: attack tools, detection tools, orchestrator, test suite

`Python` `Paramiko` `scipy` `auth.log analysis` `CVE-2016-6210` `Detection Engineering`

---

### [ThreatLens](https://github.com/Alisha-chaudhary/ThreatLens) · Python · Security Reconnaissance Framework

A modular recon framework that runs OSINT, port scanning, SSL/TLS inspection, DNS enumeration, HTTP header analysis, and CVE correlation in parallel and produces a structured HTML/PDF risk report with a calculated risk score.

**What it covers:**
- Async parallel execution via `asyncio`, a full scan without sequential waiting
- CVE lookup via NVD API + Shodan integration for exposure context
- Tech fingerprinting mapped to known vulnerabilities
- Risk scoring that distinguishes signal from noise in raw scan output

`Python` `asyncio` `Shodan API` `NVD/CVE APIs` `ReportLab` `Modular architecture`

---

### [CyberSec Labs](https://github.com/Alisha-chaudhary/CyberSec) · Python · Security Scripting Collection

Scripts covering network analysis, log parsing, regex-based IP detection, access control automation, and SQL-based threat hunting, built during self-directed study alongside the Google Cybersecurity Certificate.

`Python` `SQL` `Networking` `Log analysis` `Security automation`

---

### [BreachProbe](https://github.com/Alisha-chaudhary/BreachProbe) · Python · Breach Detection

Early-stage tooling for breach detection and exposure analysis. In active development.

`Python` `Breach analysis`

---

## Technical Skills

**Languages & Scripting** · `Python` `TypeScript` `Bash` `SQL`

**Security & Tooling** · `OSINT` `CVE Analysis` `Port Scanning` `SSL/TLS Inspection` `DNS Enumeration`
`HTTP Header Analysis` `Tech Fingerprinting` `Breach Data Analysis` `Log Parsing` `Detection Engineering`

**Frameworks & Libraries** · `React` `asyncio` `requests` `reportlab` `socket` `Shodan API` `NVD/CVE APIs`

**Platforms** · `Kali Linux` `Ubuntu` `Wireshark` `Nmap` `Burp Suite` `Metasploit` `TryHackMe` `LetsDefend`

**Concepts** · `Threat Modelling` `Risk Scoring` `OSINT Frameworks` `SOC Operations`
`Incident Response` `Secure SDLC` `OWASP Top 10` `Statistical Side-Channel Analysis`

---

## Education & Research

**B.Sc. Computer Science** · St. Francis College for Women, Osmania University, Hyderabad

**Student Researcher · Co-Author** · Dec 2024 – Jun 2025
Faculty-guided research project on AI in healthcare, resulted in a peer-reviewed publication indexed in UGC CARE Group I.

> *Artificial Intelligence in Aging Research: Advanced Models for Detecting and Targeting Cellular Senescence*
> Madhya Bharti Journal, Vol. 86, No. 7, 2025

Worked on model evaluation across Cascade R-CNN, CBAM-YOLOv3, and LSTM-CNN architectures. Contributed to feature selection analysis and multi-omics framework design.

---

## Certifications

| Certification | Issuer | Status |
|---|---|---|
| Google Cybersecurity Certificate | Google / Coursera | Completed |
| CompTIA Security+ | CompTIA | In progress |

---

## GitHub Activity

[![Alisha's GitHub Stats](https://github-readme-stats.vercel.app/api?username=Alisha-chaudhary&show_icons=true&theme=default&hide_border=true&count_private=true)](https://github.com/Alisha-chaudhary)

---

· Open to research collaborations · Building in public · [linkedin.com/in/alisha-chaudhary-](https://www.linkedin.com/in/alisha-chaudhary-/)
