# config/log_templates.py

non_issue_templates = [
    "System boot completed successfully",
    "User logged in at 10:01 AM",
    "Disk check complete, no errors found",
    "Battery level is 85%, charging",
    "Network connection established",
    "Service started successfully",
    "System update completed",
    "Drive mounted at /mnt/data",
    "Background scan completed",
    "CPU temperature within normal range",
    "No system alerts detected",
    "All services running normally",
    "WiFi connection stable",
    "Scheduled backup completed",
    "Device operating as expected"
]

issue_templates = [
    "ERROR: Battery temperature exceeds threshold",
    "WARNING: Disk usage exceeds 90%",
    "Battery drain detected, shutdown imminent",
    "CRITICAL ERROR: Kernel panic occurred",
    "WARNING: Low battery, 5% remaining",
    "ERROR: Unable to read from disk",
    "System failed to boot - error code 0x80004005",
    "Power failure detected, system shutting down",
    "ALERT: Battery health is degraded",
    "WARNING: CPU temperature high",
    "ERROR: Unexpected shutdown occurred",
    "CRITICAL: Memory leak detected",
    "ALERT: System resource usage critical",
    "ERROR: Failed to mount root partition",
    "WARNING: Fan speed below threshold"
]
