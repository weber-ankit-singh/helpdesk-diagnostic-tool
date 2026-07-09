# Helpdesk "First Responder" Diagnostic Tool

## Problem Statement
Support engineers often spend the first 15 minutes of a support call manually gathering basic system data—such as IP addresses, OS versions, and disk health—from the user's machine. This utility automates that process, providing an instant report that accelerates root-cause analysis (RCA) and ticket triage.

## Technical Overview
This script interacts directly with the local system to pull hardware and networking metrics. It provides an automated assessment of system health, specifically flagging low disk space which is a common root cause for system sluggishness.

![Architecture Diagram](python_diagnostic_scripts.png)

## Core Features
* **Automated Data Collection:** Instantly retrieves OS name, Hostname, and Local IP address.
* **Hardware Metrics:** Scans the local hard drive to report total and free storage capacity.
* **Automated Triage Warning:** Automatically flags disk space below 10GB as a potential performance bottleneck, saving the support engineer manual investigation time.

## Technical Stack
* **Language:** Python 3.x
* **Core Modules:** `platform`, `socket`, `shutil`
* **Compatibility:** Cross-platform (Windows/Linux/macOS)

## Setup & Execution
1. Clone this repository: `git clone [https://github.com/weber-ankit-singh/helpdesk-diagnostic-tool]`
2. Navigate to the project directory in your terminal.
3. Run the script: `python system_diagnostic.py`

## Use Case
To be run directly on a user's machine during an IT support session. It instantly provides the support engineer with the necessary system environment data to isolate issues faster and meet SLA response times.
# helpdesk-diagnostic-tool
