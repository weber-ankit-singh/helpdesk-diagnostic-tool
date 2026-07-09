import platform
import socket
import shutil

def generate_system_report():
    print("--- Running Helpdesk Diagnostic Tool ---\n")
    
    # 1. Get Operating System Info
    os_info = platform.system() + " " + platform.release()
    
    # 2. Get Network Info (Hostname and IP)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # 3. Get Disk Space (Checks the current drive)
    total, used, free = shutil.disk_usage(".")
    free_gb = free // (2**30) # Mathematical conversion from Bytes to Gigabytes
    total_gb = total // (2**30)
    
    # 4. Print the Clean Report for the Support Engineer
    print("--- SYSTEM DIAGNOSTIC REPORT ---")
    print(f"OS Version:   {os_info}")
    print(f"Hostname:     {hostname}")
    print(f"IP Address:   {ip_address}")
    print(f"Disk Space:   {free_gb} GB Free out of {total_gb} GB")
    
    # 5. Automated Triage Warning
    if free_gb < 10:
        print("\n[WARNING] Disk space is critically low. This may cause system slowness.")
    else:
        print("\n[OK] Disk space is healthy.")

# Run the function
if __name__ == "__main__":
    generate_system_report()

