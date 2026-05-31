# Day 3: Lists and For loops

# A list of suspicious IP addresses found in the log
suspicious_ips = ["192.168.1.50","10.0.0.1","172.16.0.4","192.168.1.50"]
target_malicious_ip = "192.168.1.50"

print("---- Automated Bulk IP Scan ----")

# The loop insppppects each IP in the list one by one
count = 0
for ip in suspicious_ips:
  print("Checking database for IP:",ip)

# Combining Day 2 logic inside our Day 3 loop
if ip == target_malicious_ip:
  print("---> MATCH FOUND: This IP is known flagged malicious!")
  count = count+1
print("---- Scan Complete ----")
print("Total malicious matches found:", count)
