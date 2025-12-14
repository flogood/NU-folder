#  Automated MITRE ATT&CK Log Mapper

## 🚀 Project Objectives and Features

This project is a Python-based security automation tool designed to enhance threat detection and analysis.

### Objectives
* Develop a robust log parsing mechanism capable of ingesting structured security logs (e.g., JSON).
* Automatically identify security-relevant events and map them to MITRE ATT&CK Tactics and Techniques.
* Generate a summarized report that clearly visualizes the observed attacker behavior, prioritizing the most critical findings.

### Key Features
* **Modular Rule Set:** Uses an expandable Python dictionary for easy rule definition.
* **Actionable Intelligence:** Transforms raw log data into immediate threat correlation insights.
* **Future-Ready:** Architecture designed for future machine learning integration for anomaly detection (stretch goal).

## 🛠️ Setup and Running Instructions

### Prerequisites
* Python 3.x installed (preferably via Anaconda)
* Visual Studio Code (VS Code)

### Dependencies
The following Python packages must be installed in your virtual environment:
1.  `mitreattack-python`
2.  `stix2`

### Setup Guide

1.  **Clone the Repository:** (You will do this step after uploading to GitHub)
    ```bash
    git clone [YOUR-REPOSITORY-URL]
    cd ATTACK_Log_Mapper
    ```
2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # macOS/Linux
    ```
3.  **Install Dependencies:**
    ```bash
    pip install mitreattack-python stix2
    ```
4.  **Provide Input:** Create a file named `sample_logs.json` containing structured security event data in the project root folder.
5.  **Run the Mapper:**
    ```bash
    python mapper.py
    ```

## 🚨 API Keys Notice
This project uses publicly available MITRE ATT&CK data and does not require any private API keys. No secrets are stored in this repository.