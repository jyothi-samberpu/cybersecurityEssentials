3. Setup and configure a basic firewall using tools like iptables on Linux.

Instead on LINUX we are doing in Python.
You can set up and configure a basic firewall using Python by interacting with iptables via the subprocess module. Below is a Python script to configure a simple firewall.

How It Works:

1. Executes iptables commands using Python’s subprocess.run().
2. Defines default policies (DROP all incoming and forwarded traffic).
3. Allows essential traffic like SSH, HTTP, and HTTPS.
4. Prevents attacks (blocks ping, port scanning, and limits SSH logins).
5. Saves the firewall rules to persist after reboot.

TO SAVE
windows_firewall.py

TO COMPILE
python windows_firewall.py

# OUTPUT:

Firewall setup complete!
