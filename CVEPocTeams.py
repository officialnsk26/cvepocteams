import requests
from datetime import datetime, timezone

# Function to fetch CVEs for a specific day
def fetch_cves(date):
    url = "https://poc-in-github.motikan2010.net/api/v1/"
    response = requests.get(url)
    if response.status_code == 200:
        cves = response.json()["pocs"]
        filtered_cves = [cve for cve in cves if cve["inserted_at"].startswith(date)]
        return filtered_cves
    else:
        print("Failed to fetch CVEs")
        return []

# Function to send a message to Microsoft Teams via webhook URL
def send_teams_message(webhook_url, message):
    payload = {
        "text": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print("Failed to send message to Teams")
    else:
        print("Message sent successfully")

# Set the date to fetch CVEs for (format: YYYY-MM-DD)
date_to_fetch = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Fetch CVEs for the specified date
cves = fetch_cves(date_to_fetch)

if cves:
    # Webhook URL for Microsoft Teams
    teams_webhook_url = "YOUR MS TEAMS WEBHOOK URL"

    # Prepare message with CVE details
    message = f"New CVE POC has been discovered on {date_to_fetch}:\n\n\n\n"

    for cve in cves:
        message += f"\n🚨 **CVE ID:** {cve['cve_id']}\n"
        message += f"\n📓 **Description:** {cve['description']}\n"
        message += f"\n🟢 **POC Owner:** {cve['owner']}\n"
        message += f"\nℹ️ **Repository Name:** {cve['full_name']}\n"
        message += f"\n📣 **POC URL:** {cve['html_url']}\n"
        message += f"\n🔓 **CVE Name:** {cve['name']}\n"
        message += f"\n📓 **Vulnerability Description:** {cve['vuln_description']}\n"
        message += f"\n📅 **POC Created At:** {cve['created_at']}\n"
        message += f"\n📅 **POC Updated At:** {cve['updated_at']}\n"
        message += f"\n📅 **POC Pushed At:** {cve['pushed_at']}\n\n"
        message += "--------------------------------------------------------------------------------------\n\n"

    # Send message to Teams
    send_teams_message(teams_webhook_url, message)
else:
    print("No CVEs reported for today")
