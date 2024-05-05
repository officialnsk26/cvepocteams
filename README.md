# CVE POC TEAMS
Use this automation bot to monitor CVE POCs from poc-in-github.motikan2010.net API and deliver notifications via MS Teams.

# Overview
CVE POC Bot is an automation tool designed to monitor Proof of Concept (POC) vulnerabilities listed on poc-in-github.motikan2010.net API and notify relevant teams through Microsoft Teams.

# Features
Automated Monitoring: Utilizes Python to automatically fetch and monitor newly discovered CVE POCs.
Integration with GitHub API: Interacts with the poc-in-github.motikan2010.net API to gather information on CVE POCs.
Microsoft Teams Integration: Sends formatted notifications to designated Microsoft Teams channels for immediate attention by relevant teams.

# Usage
Setup Python Environment: Ensure Python is installed on your system.
Install Dependencies: Install necessary dependencies using pip install -r requirements.txt.
Configure Microsoft Teams Webhook: Obtain a webhook URL for your Microsoft Teams channel and update the teams_webhook_url variable in the script.
Run the Script: Execute the script cve_poc_bot.py.
Scheduled Execution: Optionally, schedule the script to run periodically using tools like Windows Task Scheduler.

# Configuration
teams_webhook_url: Microsoft Teams webhook URL for sending notifications.
date_to_fetch: Date format used to fetch CVEs (default: current date).
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
