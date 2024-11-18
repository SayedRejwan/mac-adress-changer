# MAC Address Changer Tool

## Overview
The **MAC Address Changer Tool** is a Python-based utility designed to change (or spoof) the Media Access Control (MAC) address of a network interface on a Linux system. This can be particularly useful for purposes such as testing network configurations, enhancing privacy, or bypassing network access restrictions.

## Features
- Change the MAC address of any specified network interface.
- Validate the provided MAC address for correctness.
- Log all activities to a log file (`mac_changer.log`) for audit and debugging purposes.
- Notify the user via email of the original MAC address before making any changes.
- Works on Linux-based systems only.

## Technologies Used
- **Python** for scripting and automation.
- **subprocess**: Run shell commands to interact with network interfaces.
- **argparse**: Handle command-line arguments for ease of use.
- **re**: Regular expressions for validating MAC address format.
- **smtplib** and **MIMEText**: Send email notifications with details of the original MAC address.
- **logging**: Log all actions for troubleshooting and auditing.

## Prerequisites
- A Linux system (Ubuntu, Debian, Fedora, etc.).
- Python 3 installed.
- Root privileges are required for executing this script since changing network configurations demands superuser access.

## Installation
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/mac-address-changer-tool.git
   cd mac-address-changer-tool
   ```
2. **Install Dependencies**:
   - Python libraries used (`argparse`, `re`, `smtplib`) are part of the Python standard library and do not require additional installation.

## Usage
To run the script, open a terminal and navigate to the directory containing the script.

```sh
sudo python mac_changer.py -i <interface> -m <new_mac_address>
```
### Example
```sh
sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

### Command-Line Arguments
- `-i`, `--interface`: The name of the network interface whose MAC address you want to change (e.g., `eth0`, `wlan0`).
- `-m`, `--mac`: The new MAC address you want to assign, formatted as `XX:XX:XX:XX:XX:XX`.

### Email Notification
The script is configured to send an email to `sayedrejwanur@gmail.com` with details of the original MAC address before making any changes. Update the SMTP credentials in the script before running.

## Important Notes
- **Root Access**: This script requires root access. Make sure to run it using `sudo`.
- **App Password**: To send an email through Gmail, you need to generate an **App Password** in your Google Account settings. Replace the placeholders in the script (`smtp_user` and `smtp_password`) with your own credentials.

## Logging
All actions performed by the script are logged to `mac_changer.log`. Logs include:
- Changes in MAC address.
- Errors encountered during the process.
- Email notification status.

## Disclaimer
This tool is intended for educational and testing purposes only. Unauthorized use of this tool on networks or systems without permission is illegal. Please use it responsibly.

## Contributing
Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or further information, please contact **Sayed Rejwanur Rahman** at **sayedrejwanur@gmail.com**.

