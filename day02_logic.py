# Day 2 : Conditionals (If/Else)

login_attempts = 4
max_allowed = 3
user_status = "locked"

print("---- Automated Security Check ----")

# Decision Tree 2: Checking numbers
if login_attempts > max_allowed:
  print("ALERT: Potential brute force attack detected.Blocking IP.")
elif login_attempts == max_allowed:
  print("WARNING: Final attempt. Lockout iminent.")
else:
  print("Status Normal. Awaiting login.")

#Decision Tree 2: Checking text
if user_status == "locked":
  print("ACTION: Account disabled. Administrator intervention required.")
else:
  print("ACTION: No action required.")
  
