4. Demonstrate DNS spoofing and DNS cache poisoning attacks.

# PROGRAM:

Simulated DNS Spoofing in C
This program constructs and sends a fake DNS response to simulate a DNS spoofing attack. A DNS server is tricked into associating a domain name with a malicious IP.

# Key Notes:

1. Controlled Environment Only: Run this code in a lab environment where you have permission to conduct experiments. Use isolated networks like virtual machines or a sandbox environment.
2. Ethical Responsibility: Use this knowledge only for educational purposes and to strengthen security systems.
3. Understanding Legality: Unauthorized DNS spoofing or cache poisoning is illegal in most jurisdictions.

# COMPILE AND EXECUTION :

SAVE: dns.py
Compile: python dns.py

# OUTPUT :

--- Normal DNS Resolution ---
[✅] Resolving example.com: 93.184.216.34

--- Simulating DNS Cache Poisoning Attack ---
[⚠️] DNS Cache Poisoned! example.com now resolves to 192.168.1.100

--- Post-Attack Resolution ---
[✅] Resolving example.com: 192.168.1.100

--- Cache Expiring... ---
[♻️] DNS Cache Restored!

--- Final DNS Resolution ---
[✅] Resolving example.com: 93.184.216.34
