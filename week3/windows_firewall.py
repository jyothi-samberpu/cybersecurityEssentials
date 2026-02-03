import subprocess
def run_command(command):
    """Execute a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def setup_firewall():
    print("Setting up basic firewall using iptables...")

    # Set default policies
    run_command("sudo iptables -P INPUT DROP")
    run_command("sudo iptables -P FORWARD DROP")
    run_command("sudo iptables -P OUTPUT ACCEPT")

    # Allow established and related connections
    run_command("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")

    # Allow loopback interface (localhost)
    run_command("sudo iptables -A INPUT -i lo -j ACCEPT")

    # Allow SSH (port 22)
    run_command("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")

    # Allow HTTP (port 80) and HTTPS (port 443)
    run_command("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")
    run_command("sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT")

    # Block ping requests
    run_command("sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP")

    # Block common port scan patterns
    run_command("sudo iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP")
    run_command("sudo iptables -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP")
    run_command("sudo iptables -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")

    # Rate limit SSH login attempts
    run_command("sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 3/min --limit-burst 3 -j ACCEPT")

    # Save firewall rules
    run_command("sudo iptables-save | sudo tee /etc/iptables/rules.v4")

    print("Firewall setup complete!")

if __name__ == "__main__":
    setup_firewall()