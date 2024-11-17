import subprocess
import argparse
import re
import logging
import os
import platform
import smtplib
from email.mime.text import MIMEText

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='mac_changer.log', filemode='a')

def get_arguments():
    parser = argparse.ArgumentParser(description="A tool to change the MAC address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address in format (XX:XX:XX:XX:XX:XX)")
    return parser.parse_args()

def check_root_privileges():
    if os.geteuid() != 0:
        logging.error("[-] This script requires root privileges. Please run with sudo.")
        exit(1)

def change_mac(interface, new_mac):
    try:
        logging.info(f"[+] Changing MAC address for {interface} to {new_mac}")
        subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
        subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac], check=True)
        subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
        logging.info(f"[+] MAC address for {interface} changed successfully to {new_mac}")
    except subprocess.CalledProcessError as e:
        logging.error(f"[-] Failed to change MAC address for {interface}: {e}")
        exit(1)

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ip", "link", "show", interface]).decode('utf-8')
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_address_search_result:
            mac_address = mac_address_search_result.group(0)
            logging.info(f"[+] Retrieved current MAC address for {interface}: {mac_address}")
            return mac_address
        else:
            logging.error("[-] Could not read MAC address for interface {interface}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"[-] Error: Could not run ip on the specified interface {interface}: {e}")
    return None

def validate_mac(mac):
    mac_regex = re.compile(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$")
    if mac_regex.match(mac):
        logging.info(f"[+] Provided MAC address {mac} is valid.")
        return True
    else:
        logging.error(f"[-] Provided MAC address {mac} is invalid.")
        return False

def send_email(original_mac):
    default_email = "sayedrejwanur@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "sayedrahman123123@gmail.com"
    smtp_password = "mhdg xsme xcxn pxxh"
    
    try:
        subject = "Original MAC Address"
        body = f"The original MAC address was: {original_mac}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_user
        msg['To'] = default_email

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, default_email, msg.as_string())
        server.quit()
        logging.info(f"[+] Sent original MAC address to {default_email}")
    except Exception as e:
        logging.error(f"[-] Failed to send email: {e}")

check_root_privileges()

options = get_arguments()

if not validate_mac(options.new_mac):
    logging.error("[-] Invalid MAC address format. Please enter the MAC address in the correct format (e.g., 00:11:22:33:44:55).")
    exit(1)

current_mac = get_current_mac(options.interface)
if current_mac:
    logging.info(f"[+] Current MAC address for {options.interface} is: {current_mac}")

if current_mac:
    send_email(current_mac)

change_mac(options.interface, options.new_mac)

updated_mac = get_current_mac(options.interface)
if updated_mac == options.new_mac:
    logging.info(f"[+] MAC address was successfully changed to {updated_mac}")
else:
    logging.error("[-] MAC address did not get changed.")

if platform.system() == "Windows":
    logging.error("[-] This script is designed for Linux-based systems. Windows is not supported.")
    exit(1)
