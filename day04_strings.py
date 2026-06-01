# Day 4: String Manipulation

# A raw, messy log line (notice the extra spaces at the beginning and end)
raw_log_line = "   May 31 08:14:22 server1 sshd: Failed password for admin from 103.45.67.89   "

print("--- Log String Extraction ---")

# 1. Strip: Cleans up the invisible whitespace and newlines at the edges
clean_line = raw_log_line.strip()
print("Cleaned Line:", clean_line)

# 2. In: Searches for a specific substring within the main string
if "Failed password" in clean_line:
    print("ALERT: Authentication failure detected.")

# 3. Split: Chops the string into a list of individual words, cutting at every space
words = clean_line.split()
print("Total parts in the log line:", len(words))

# 4. Indexing: Grabbing specific data
# In Python lists, counting starts at 0. But you can also count backwards.
# index -1 always grabs the very last item in the list.
attacker_ip = words[-1]
target_user = words[8] # The 9th word in the sentence

print("Targeted User:", target_user)
print("Extracted Attacker IP:", attacker_ip)
