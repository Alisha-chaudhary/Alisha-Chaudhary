# Alisha Chaudhary

### Cybersecurity Analyst · Threat Intelligence · Vulnerability Research · Security Automation

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Alisha--Chaudhary-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alisha-chaudhary-/)
[![Location](https://img.shields.io/badge/Location-Hyderabad%2C%20India-informational?style=flat&logo=googlemaps&logoColor=white)](https://github.com/Alisha-chaudhary)

---

## About Me

I came into cybersecurity from a science background - a B.Sc. in Computer Science with coursework spanning Python, Java, databases, and data structures, not from a traditional security or CS-heavy track. What I've found is that the habits from a science background transfer directly, form a hypothesis, build a controlled environment to test it, measure the result, and write down what actually happened, including the parts that didn't work.

That approach is the throughline in my projects. In `ssh-enum`, I didn't just confirm a vulnerability exists - I used Welch's t-test and Cohen's d to statistically measure whether timing differences in OpenSSH responses were significant enough to be exploitable. That's a methodology I picked up from research work, applied to a security question.

I'm currently applying to Master's programmes in Cybersecurity to build the theoretical depth, network security, applied cryptography, risk management - behind what I've been teaching myself hands-on through labs, CVE research, and the Google Cybersecurity Certificate.

---

## Projects

### [ThreatLens](https://github.com/Alisha-chaudhary/ThreatLens) — Python · Security Reconnaissance Tool
A modular reconnaissance framework that runs OSINT gathering, port scanning, SSL/TLS checks, DNS enumeration, HTTP header analysis, and tech fingerprinting against a target domain in parallel, then maps findings to known CVEs and compiles everything into a structured HTML/PDF report with a calculated risk score. The focus was as much on making results usable as on the scanning itself.

`Python` `asyncio` `Shodan API` `NVD/CVE APIs` `PDF reporting`

### [ssh-enum](https://github.com/Alisha-chaudhary/ssh-enum) — Python · CVE Research
Investigates whether OpenSSH still leaks valid usernames through response or timing differences (CVE-2016-6210), reproduced in a controlled Ubuntu 22.04.5 lab. Timing differences are evaluated using Welch's t-test and Cohen's d rather than eyeballed, and a Python detection pipeline flags enumeration patterns from authentication logs.

`Python` `CVE Research` `Statistical Analysis` `Detection Engineering`

### [CyberSec](https://github.com/Alisha-chaudhary/CyberSec) — Python & SQL · Security Scripting Toolkit
A collection of scripts built during the Google Cybersecurity Certificate, covering log analysis, regex-based IP detection, access control automation, and SQL-based threat hunting.

`Python` `SQL` `Log Analysis` `Automation`

### [TryHackMe Writeups](https://github.com/Alisha-chaudhary/TryHackMe-Writeups)
Documentation of labs worked through on TryHackMe, focused on the reasoning process - What was tried, what failed, what that revealed rather than just final answers.

`CTF` `Documentation` `Network Security`

---

## What's Next

I'm in the early planning stages of an AI-assisted SIEM copilot, an assistant that would query sources like Shodan and VirusTotal directly and surface a condensed verdict (e.g. flagging poor IP/domain reputation) instead of requiring an analyst to cross-reference each source manually. Nothing's built yet, right now I'm scoping the integrations and what a useful output actually looks like before writing code.

---

## Open Source

My first pull request went to the MITRE ATT&CK Python library - it fixed an `AttributeError` and added regression tests, currently under maintainer review.

---

## Skills

**Languages:** Python · SQL · JavaScript
**Security:** CVE Analysis · OSINT · Port Scanning · SSL/TLS Inspection · DNS Enumeration · Threat Intelligence · MITRE ATT&CK · OWASP Top 10
**Tools:** Wireshark · Nmap · Burp Suite · Shodan · Git · Metasploit
**Platforms:** Kali Linux · Ubuntu · VMware Workstation Pro

---

## Background

**B.Sc. Computer Science** — St. Francis College for Women (Osmania University), Hyderabad

**Student Researcher / Co-Author** — Dec 2024 – Jun 2025
Co-authored a UGC CARE Group I–indexed paper evaluating deep learning models (Cascade R-CNN, CBAM-YOLOv3, LSTM-CNN hybrids) for pattern detection, reaching up to 99.10% accuracy in specific cases.
*"Artificial Intelligence in Aging Research: Advanced Models for Detecting and Targeting Cellular Senescence"* —> Madhya Bharti Journal, Vol. 86, No. 7, 2025

**Google Cybersecurity Professional Certificate**

---

## GitHub Stats

[![Alisha's GitHub Stats](https://github-readme-stats.vercel.app/api?username=Alisha-chaudhary&show_icons=true&theme=default&hide_border=true&count_private=true)](https://github.com/Alisha-chaudhary)

---

## Let's Connect

Open to cybersecurity research collaborations, open-source contributions, and conversations about MSc programmes.

- **LinkedIn:** [linkedin.com/in/alisha-chaudhary-](https://www.linkedin.com/in/alisha-chaudhary-/)
- **GitHub:** [github.com/Alisha-chaudhary](https://github.com/Alisha-chaudhary)
