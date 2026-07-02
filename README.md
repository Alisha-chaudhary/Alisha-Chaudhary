# Hi, I'm Alisha Chaudhary 👋

### Cybersecurity Analyst | Threat Intelligence | Vulnerability Assessment | CVE Research | Security Research

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"/>
  <img src="https://img.shields.io/badge/Threat_Intelligence-00599C?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/CVE_Research-DC2626?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/MITRE_ATT%26CK-6A1B9A?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Open_Source-181717?style=for-the-badge&logo=github"/>
</p>

---

## About

I build practical security tools, investigate published vulnerabilities through controlled experimentation, and translate technical findings into actionable defensive intelligence.

My work focuses on **threat intelligence, vulnerability assessment, CVE research, and security automation**. Rather than accepting published security claims at face value, I enjoy validating them through reproducible experimentation, careful measurement, and transparent reporting.

With a multidisciplinary background in **Computer Applications, Biochemistry, and Chemistry**, I approach cybersecurity as an evidence-driven discipline: formulate a hypothesis, build a controlled environment, measure the outcome, and document findings that others can reproduce.

---

# 🔬 Featured Projects

## 🔐 ssh-enum
### Statistical Validation Study of CVE-2016-6210

<p>
<img src="https://img.shields.io/badge/CVE-2016--6210-red?style=flat-square"/>
<img src="https://img.shields.io/badge/OpenSSH-Tested-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Welch's_t--test-Statistical_Analysis-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Cohen's_d-Effect_Size-orange?style=flat-square"/>
</p>

> **Research Summary**
>
> **Objective:** Re-evaluate CVE-2016-6210 on a modern default OpenSSH deployment.
>
> **Method:** Manual probing, Hydra, and Metasploit were used to collect authentication timing measurements. Welch's *t*-test and Cohen's *d* were applied to distinguish genuine timing signals from measurement noise.
>
> **Finding:** No statistically significant timing difference was observed on the tested Ubuntu Server default PAM configuration, indicating that the documented timing side-channel was not reproducible under these conditions.

This project re-investigates **CVE-2016-6210**, an OpenSSH username enumeration timing side-channel, to determine whether it remains observable on a modern Ubuntu Server configured with default PAM authentication.

Rather than relying on visual inspection of response times, the project evaluates timing measurements statistically. The outcome is a reproducible validation study demonstrating that carefully supported negative results can be as valuable as positive findings when assessing the current security posture of published vulnerabilities.

**Stack**

`Python` • `OpenSSH` • `Hydra` • `Metasploit` • `Ubuntu Server` • `Kali Linux`

---

## 🔍 ThreatLens

Python-based vulnerability assessment platform integrating reconnaissance, CVE intelligence, weighted risk scoring, and automated reporting into a single workflow.

Features include:

- DNS Enumeration
- SSL/TLS Inspection
- HTTP Security Header Analysis
- Technology Fingerprinting
- OSINT Integration
- CVE Correlation
- HTML/PDF Reporting

**Stack**

`Python` • `AsyncIO` • `NVD API` • `Shodan` • `HTML` • `PDF`

---

## 📑 CVE Threat Intelligence Reports

Technical reports analysing recent vulnerabilities through:

- CVSS Assessment
- MITRE ATT&CK Mapping
- Exploitation Context
- Indicators of Compromise
- Detection Opportunities
- Defensive Recommendations

---

## 🛡️ CyberSec Toolkit

Collection of Python and SQL security scripts covering log analysis, detection engineering exercises, access control automation, and introductory threat hunting.

---

# 📚 Research

### Artificial Intelligence in Aging Research: Advanced Models for Detecting and Targeting Cellular Senescence

Co-author of a peer-reviewed publication investigating deep learning approaches for cellular senescence detection.

**Published in**

**Madhya Bharti Journal**

UGC CARE Group I

Vol. 86, No. 7 (2025)

---

# 🌍 Open Source

Contributed to the official **MITRE ATT&CK Python library** by:

- Identifying an AttributeError in the navlayers exporter
- Implementing the fix
- Expanding automated regression test coverage
- Submitting a pull request currently under maintainer review

---

# 💻 Technical Skills

### Languages

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![C](https://img.shields.io/badge/C-00599C?style=flat-square)

### Security

![Threat Intelligence](https://img.shields.io/badge/Threat_Intelligence-blue?style=flat-square)
![Vulnerability Assessment](https://img.shields.io/badge/Vulnerability_Assessment-red?style=flat-square)
![CVE Research](https://img.shields.io/badge/CVE_Research-darkred?style=flat-square)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-purple?style=flat-square)
![NIST CSF](https://img.shields.io/badge/NIST_CSF-005BBB?style=flat-square)
![OWASP Top 10](https://img.shields.io/badge/OWASP_Top_10-black?style=flat-square)

### Tools

![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-00457C?style=flat-square)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square)
![Metasploit](https://img.shields.io/badge/Metasploit-2596CD?style=flat-square)
![Hydra](https://img.shields.io/badge/Hydra-555555?style=flat-square)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

### Platforms

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali-557C94?style=flat-square&logo=kalilinux&logoColor=white)
![VMware](https://img.shields.io/badge/VMware-607078?style=flat-square)

---

# 🌱 Currently Exploring

- Infrastructure Security
- Detection Engineering
- Threat Hunting
- Applied Cryptography
- Cloud Security

---

# 📊 GitHub Analytics

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=Alisha-chaudhary&show_icons=true&rank_icon=github&theme=transparent"/>
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Alisha-chaudhary&layout=compact&theme=transparent"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Alisha-chaudhary&theme=transparent"/>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Alisha-chaudhary&label=Profile%20Views&color=0e75b6&style=flat"/>
</p>

---

# 🤝 Let's Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Alisha_Chaudhary-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/alisha-chaudhary-/)

[![GitHub](https://img.shields.io/badge/GitHub-Alisha--chaudhary-181717?style=for-the-badge&logo=github)](https://github.com/Alisha-chaudhary)

I'm always interested in cybersecurity research, vulnerability analysis, open-source collaboration, and conversations about infrastructure security and threat intelligence.
