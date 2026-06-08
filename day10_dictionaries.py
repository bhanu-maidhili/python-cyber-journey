# Day 10: Dictionaries (Key-Value pairs)

print("--- IP Threat Tracking Engine ---")

# A simulated list of IPs extracted by our regex (notice the repeats)
extracted_ips = ["192.168.1.50","10.0.0.5","192.168.1.50","192.168.1.50","10.0.0.5","8.8.8.8"]

# We create an empty dictionary using curly braces {}
threat_counts = {}

# We loop through the list of IPs one by one 
for ip in extracted_ips:
  # If the IP is ALREADY in our dictionary, add 1 to its current count
  if ip in threat_counts:
    threat_counts[ip] = threat_counts[ip]+1
    # If this is the FIRST time seeing the IP, add it to the dictionary with a count of 1
  else:
    threat_counts[ip] = 1

print("--- Final Threat Summary ---")
# Loop through the dictionary to print a clean report
for target_ip, count in threat_counts.items():
  print(f"IP: {target_ip} | Total Attacks: {count}")
  
