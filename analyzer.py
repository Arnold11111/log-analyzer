import re

def analyze_log(file_path):
    suspicious = []

    try:
        with open(file_path, "r") as log_file:
            for line in log_file:
                # Detect repeated failed SSH login attempts
                if "Failed password" in line or "authentication failure" in line:
                    suspicious.append(line.strip())

    except FileNotFoundError:
        print("❌ Log file not found.")
        return

    print("\n🔍 Suspicious Entries Detected:")
    if suspicious:
        for entry in suspicious:
            print(f"⚠️ {entry}")
    else:
        print("✅ No suspicious activity found.")

if __name__ == "__main__":
    path = input("Enter path to log file (e.g., /var/log/auth.log): ")
    analyze_log(path)
