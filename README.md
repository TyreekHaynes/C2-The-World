# Advanced C2 Infrastructure

Adversary Emulation C2 Framework for Red Team Training & Defensive Validation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?logo=Cloudflare&logoColor=white)](https://cloudflare.com)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## LEGAL DISCLAIMER

**FOR AUTHORIZED SECURITY TESTING AND EDUCATIONAL PURPOSES ONLY**

This infrastructure is designed for:
- Authorized penetration testing
- Red team operations
- Security research
- Educational demonstrations

**NEVER** deploy this infrastructure against systems you do not own or have explicit written permission to test.

## Architecture Overview
┌─────────────────────────────────────────────────────────────┐
│ PUBLIC INTERNET │
└──────────────────────────┬──────────────────────────────────┘
│
[ DNS Queries ]
│
┌──────────────────────────▼──────────────────────────────────┐
│ CLOUD DNS INFRASTRUCTURE │
│ (Cloudflare) │
│ • Domain: assets-delivery.org │
│ • DDoS Protection │
│ • SSL/TLS Termination │
└──────────────────────────┬──────────────────────────────────┘
│
[ HTTPS Traffic ]
│
┌──────────────────────────▼──────────────────────────────────┐
│ REDIRECTOR LAYER │
│ (Nginx - AWS) │
│ • Public Subnet │
│ • Elastic IP: 3.150.196.7 │
│ • SSL Termination │
│ • Request Forwarding │
└──────────────────────────┬──────────────────────────────────┘
│
[ Internal Network ]
│
┌──────────────────────────▼──────────────────────────────────┐
│ C2 TEAMSERVER │
│ (FastAPI - AWS) │
│ • Private Subnet │
│ • No Public IP │
│ • Agent Management │
│ • Task Orchestration │
│ • Encrypted Communications │
└──────────────────────────┬──────────────────────────────────┘
│
[ Agent Tasks ]
│
┌──────────────────────────▼──────────────────────────────────┐
│ AGENTS │
│ (Windows/Linux/macOS Targets) │
│ • Python-based implants │
│ • Encrypted C2 communications │
│ • Module-based architecture │
│ • Persistence mechanisms │
└─────────────────────────────────────────────────────────────┘
