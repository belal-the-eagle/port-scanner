# port-scanner
### Simple Port Scanner

A lightweight and fast network port scanner written in Python. It allows you to scan either a single specific port or a custom range of ports on a target IP address. 

### Features

* **Single Port Scan**: Check if a specific port is open or closed.
* **Custom Range Scan**: Scan a range of ports sequentially.
* **Visual Interface**: Features a beautiful stylized ASCII banner and color-coded output (Green for Open, Red for Closed) using colorama and pyfiglet.
* **Timeout Protection**: Includes a connection timeout to speed up the scanning process.

### Prerequisites

Make sure you have Python 3 installed on your system. You will also need to install the required external libraries. 

### Installation

1. Clone this repository: 

bash

git clone https://github.com/belal-the-eagle/port-scanner.git

cd port-scanner

2. Install the dependencies using the provided requirements file: 

bash

pip install -r requirements.txt

### Usage

You can run the script in two different modes: 

### 1. Scan a Single Port

bash

python port-scanner.py <target_ip> <target_port>

*Example:* python port-scanner.py 192.168.1.1 80 

### 2. Scan a Range of Ports

bash

python port-scanner.py <target_ip> <from_port> <to_port>

*Example:* python port-scanner.py 192.168.1.1 20 80 

### Disclaimer

This tool is developed for educational and authorized security testing purposes only. Do not use it against targets without prior written consent.
