import speedtest
import time
from datetime import datetime
# TODO pip install speedtest_cli

def log_internet_speed():
    try:
        # Create a Speedtest instance
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"down/up speeds in Mbps: {download_speed} | {upload_speed}")
    except Exception as e:
        print(f"Error: {e}")
        download_speed = 0.0
        upload_speed = 0.0

    # Log the speeds to a file
    with open("internet_speed_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps\n")

    print(f"Logged: Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")


# Run the log every 30 minutes
while True:
    log_internet_speed()
    time.sleep(1800)