# CyberShield — Basic Cybersecurity Monitoring Dashboard

CyberShield is a beginner-friendly, browser-based dashboard built with Python, Streamlit, and pandas. It demonstrates how login records can be reviewed for successful and failed sign-ins and how repeated failures from one IP can be highlighted for further review.

> **Important:** This project uses fictional sample records only. It does not monitor a real computer, collect real credentials, scan networks, or prove that an IP is malicious.

## Features
- 20 synthetic login records with timestamp, username, IP address, result, and location.
- Summary metrics for total, successful, and failed login events.
- Bar chart for success/failure counts.
- Filters for result, username, and IP address.
- CSV download of the filtered login history.
- Simple suspicious-activity rule: flag an IP with 3 or more failed attempts in the sample data.

## Project files
- `app.py` — Streamlit application and sample data.
- `requirements.txt` — Python dependencies.
- `Project_Report.pdf` — project report.
- `README.md` — setup and usage instructions.

## Requirements
- Python 3.10 or newer recommended.
- Internet access only to install the Python packages (the app itself runs locally).

## Setup and run
1. Extract the project ZIP.
2. Open a terminal in the extracted `CyberShield_Project` folder.
3. Create and activate a virtual environment (recommended).

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the dashboard:
   ```bash
   streamlit run app.py
   ```
6. Streamlit will show a local address, usually `http://localhost:8501`. Open it in your browser.

## How to use
1. Use the sidebar to filter by login result or username.
2. Optionally enter part of an IP address.
3. Review the metrics, chart, and login history.
4. Select **Download filtered history (CSV)** to save the visible records.
5. Review the suspicious activity table. The current demonstration threshold is at least 3 failed attempts per IP across the sample dataset.

## Troubleshooting
- If `streamlit` is not recognized, activate the virtual environment and run `python -m pip install -r requirements.txt`.
- If port 8501 is busy, Streamlit may offer another local port.
- Use Python 3.10+ if package installation fails.

## Limitations and future improvements
- Data is static and fictional; it is not connected to operating-system or application logs.
- The simple threshold can create false positives and does not use a time window.
- Future work could include importing authorized log files, time-window rules, authentication, audit logging, tests, and role-based access controls.

## License
Educational/demo use. Add a license file if you plan to publish or distribute the project under a specific license.
