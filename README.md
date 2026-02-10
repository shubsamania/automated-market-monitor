**Automated Market Monitor (AI Agent)**
**
Project Overview**

In fast-moving markets (like automotive inventory or crypto), manual monitoring is inefficient. I built this automated agent to track price variance in real-time and trigger alerts only when specific statistical thresholds are met.

The Tech Stack
Orchestration: n8n (Workflow Automation)

Logic Layer: Python (Pandas for statistical variance)

Data Source: REST API (Simulated Market Data)

Alerting: Slack Webhook

The Workflow Logic
Ingest: Scheduled HTTP Request fetches JSON market data every hour.

Transform: Python script calculates the 7-day moving average and identifies outliers (>5% variance).

Decision: Conditional logic filters noise to prevent alert fatigue.

Act: High-priority anomalies are sent to Slack; raw data is logged to Google Sheets for historical analysis.

Workflow Visualization
Scroll down and click Commit changes.
