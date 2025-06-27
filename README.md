# Auto Deploy Test
# Testing Fix
# Trigger working check

## 🔧 Backend Project Description (GCP)

The backend of the Weather Alert App is a serverless, event-driven system built entirely on Google Cloud Platform (GCP). It is designed to fetch real-time weather data, analyze it for severe conditions, and trigger user alerts automatically. The architecture is fully automated, scalable, and cost-efficient, using core GCP services such as Cloud Functions, Cloud Scheduler and Pub/Sub.

### ⚙️ Core Components & Workflow:
1. **Cloud Scheduler** – triggers periodic data fetch.
2. **Cloud Function: Weather Fetcher** – fetches weather and checks for alerts.
3. **Pub/Sub** – passes alert messages.
4. **Cloud Function: Alert Dispatcher** – sends notifications.

### 🛠️ GCP Services Used:

| Service         | Purpose                                   |
|----------------|--------------------------------------------|
| Cloud Functions | Serverless compute                        |
| Cloud Scheduler | Time-based trigger                        |
| Pub/Sub         | Messaging system                          |
| Secret Manager  | API key security                          |
| Cloud Logging   | Monitoring & debugging                    |

# Currently Not Working
