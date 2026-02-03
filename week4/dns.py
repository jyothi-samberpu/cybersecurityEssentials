import time

# Simulated DNS Cache
dns_cache = {
    "example.com": "93.184.216.34",  # Legitimate IP
    "google.com": "142.250.190.14",  # Legitimate Google IP
}

def resolve_domain(domain):
    """Function to resolve a domain from the DNS cache."""
    if domain in dns_cache:
        print(f"[✅] Resolving {domain}: {dns_cache[domain]}")
    else:
        print(f"[❌] {domain} not found in cache. Fetching from real DNS...")

def poison_dns_cache(domain, fake_ip):
    """Function to simulate DNS cache poisoning."""
    dns_cache[domain] = fake_ip
    print(f"[⚠️] DNS Cache Poisoned! {domain} now resolves to {fake_ip}")

# Normal Resolution
print("\n--- Normal DNS Resolution ---")
resolve_domain("example.com")

# Simulated Attack: Poisoning the Cache
print("\n--- Simulating DNS Cache Poisoning Attack ---")
poison_dns_cache("example.com", "192.168.1.100")  # Fake malicious IP

# After Attack: Checking the resolution
print("\n--- Post-Attack Resolution ---")
resolve_domain("example.com")

# Simulating a cache expiration after some time
print("\n--- Cache Expiring... ---")
time.sleep(3)  # Simulating time passing
dns_cache["example.com"] = "93.184.216.34"  # Restoring legitimate IP
print("[♻️] DNS Cache Restored!")

# Final Resolution
print("\n--- Final DNS Resolution ---")
resolve_domain("example.com")

