"""
CyberShield: A basic local cybersecurity monitoring dashboard.
All records are synthetic demo data. This is an educational project, not a real IDS.
Run: streamlit run app.py
"""
from datetime import datetime
from io import StringIO
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CyberShield | Security Dashboard", page_icon="🛡️", layout="wide")

# Synthetic records for demonstration only. No real users or IP activity is monitored.
SAMPLE_LOGINS = [
    ("2026-10-26 08:02:11", "aisha", "192.168.1.12", "Success", "Bengaluru"),
    ("2026-10-26 08:05:34", "rahul", "192.168.1.15", "Success", "Raichur"),
    ("2026-10-26 08:10:02", "admin", "192.168.1.20", "Failed", "Unknown"),
    ("2026-10-26 08:11:19", "admin", "192.168.1.20", "Failed", "Unknown"),
    ("2026-10-26 08:12:03", "admin", "192.168.1.20", "Failed", "Unknown"),
    ("2026-10-26 08:14:45", "yasin", "192.168.1.18", "Success", "Raichur"),
    ("2026-10-26 08:18:22", "priya", "192.168.1.23", "Success", "Hyderabad"),
    ("2026-10-26 08:21:06", "guest", "203.0.113.45", "Failed", "Unknown"),
    ("2026-10-26 08:22:30", "guest", "203.0.113.45", "Failed", "Unknown"),
    ("2026-10-26 08:23:10", "guest", "203.0.113.45", "Failed", "Unknown"),
    ("2026-10-26 08:29:51", "meera", "192.168.1.27", "Success", "Chennai"),
    ("2026-10-26 08:33:04", "arjun", "192.168.1.30", "Success", "Bengaluru"),
    ("2026-10-26 08:37:42", "admin", "198.51.100.77", "Failed", "Unknown"),
    ("2026-10-26 08:39:00", "admin", "198.51.100.77", "Failed", "Unknown"),
    ("2026-10-26 08:44:12", "fatima", "192.168.1.33", "Success", "Hyderabad"),
    ("2026-10-26 08:48:58", "sanjay", "192.168.1.36", "Success", "Raichur"),
    ("2026-10-26 08:52:27", "guest", "203.0.113.45", "Failed", "Unknown"),
    ("2026-10-26 09:01:13", "nisha", "192.168.1.40", "Success", "Bengaluru"),
    ("2026-10-26 09:05:49", "admin", "198.51.100.77", "Failed", "Unknown"),
    ("2026-10-26 09:12:16", "vikram", "192.168.1.44", "Success", "Mysuru"),
]
COLUMNS = ["Timestamp", "Username", "IP Address", "Result", "Location"]

@st.cache_data
def load_demo_data():
    return pd.DataFrame(SAMPLE_LOGINS, columns=COLUMNS)

st.markdown("""
<style>
.main {background-color: #f7f9fc;}
.block-container {padding-top: 1.4rem;}
div[data-testid="stMetric"] {background: white; padding: 15px; border-radius: 10px; border: 1px solid #e4e8ef;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ CyberShield")
st.caption("Local cybersecurity monitoring dashboard • Synthetic sample data • Educational use only")

with st.sidebar:
    st.header("Filters")
    st.write("Filter the sample login history below.")
    data = load_demo_data()
    result_options = st.multiselect("Login result", ["Success", "Failed"], default=["Success", "Failed"])
    user_options = sorted(data["Username"].unique().tolist())
    selected_users = st.multiselect("Username", user_options, default=user_options)
    search_ip = st.text_input("Search IP address", placeholder="e.g. 203.0.113.45")
    st.divider()
    st.info("This demo does not monitor a real system or connect to a network.")

filtered = data[data["Result"].isin(result_options) & data["Username"].isin(selected_users)].copy()
if search_ip.strip():
    filtered = filtered[filtered["IP Address"].str.contains(search_ip.strip(), case=False, na=False)]

total = len(filtered)
success_count = int((filtered["Result"] == "Success").sum())
failed_count = int((filtered["Result"] == "Failed").sum())
failed_rate = (failed_count / total * 100) if total else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Login events", total)
c2.metric("Successful logins", success_count)
c3.metric("Failed logins", failed_count)
c4.metric("Failed rate", f"{failed_rate:.1f}%")

st.subheader("Login activity")
if filtered.empty:
    st.warning("No records match the selected filters.")
else:
    counts = filtered["Result"].value_counts().reindex(["Success", "Failed"], fill_value=0)
    st.bar_chart(counts)

st.subheader("Login history")
st.dataframe(filtered, use_container_width=True, hide_index=True)

csv_bytes = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇️ Download filtered history (CSV)",
    data=csv_bytes,
    file_name="cybershield_login_history.csv",
    mime="text/csv",
    disabled=filtered.empty,
)

st.subheader("Suspicious activity review")
st.write("The demo flags an IP when it has at least 3 failed login attempts in the displayed dataset.")
failed_by_ip = data[data["Result"] == "Failed"].groupby("IP Address").size().reset_index(name="Failed attempts")
suspicious = failed_by_ip[failed_by_ip["Failed attempts"] >= 3].sort_values("Failed attempts", ascending=False)
if suspicious.empty:
    st.success("No IP addresses meet the demo threshold.")
else:
    st.warning("Potentially suspicious IPs found in the synthetic sample data.")
    st.dataframe(suspicious, use_container_width=True, hide_index=True)

with st.expander("How to interpret this dashboard"):
    st.markdown("""
    - **Success / Failed:** result of a simulated login attempt.
    - **Failed rate:** failed attempts divided by all filtered events.
    - **Potentially suspicious IP:** an IP with at least three failed attempts in the full sample data.
    - The threshold is a simple teaching example, not proof of an attack. Real security monitoring needs authenticated log sources, time-window analysis, access controls, and privacy safeguards.
    """)

st.caption("CyberShield student project • No database required • Data is fictional and stored in the source file.")
