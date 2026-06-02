# Day 5: Functions (Reusable code Blocks)

# 1. DEFINING THE FUNCTION (Building themachine)
# We use 'def' to create a function. 'log_line' is the raw material we will feed it.

def extract_ip(log_line):
  clean_line = log_line.strip()
  words = clean_line.split()
  
  # We grab the last word (the IP)
  attacker_ip = words[-1]
  
  # 'return' is the machine spitting out the final product
  return attacker_ip
print("--- Log Parsing Function Test ---")

# 2. CALLING THE FUNCTION (Using the machine)
# Here are two different messy log lines
log_event_1 = "  May 31 08:14:22 server sshd: Failed password for admin from 103.45.67.89  "
log_event_2 = " May 31 08:18:44 server sshd: Failed password for root from 45.33.22.11 "

# We feed the logs into our custom function and save the output to new variables
ip_1 = extract_ip(log_event_1)
ip_2 = extract_ip(log_event_2)

# Printing the results
print("First attacker IP:",ip_1)
print("Second attacker IP:",ip_2)
