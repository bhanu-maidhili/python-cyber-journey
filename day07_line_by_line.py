# Day 7: Memory Efficient File Reading

target_file = "sample.log"
line_count = 0

print(f"--- Scanning {target_file} ---")

try:
  with open(target_file,"r") as file:
    # This loop pulls exactly one line into memory at a time,processes it,deletes it.
    for line in file:
      line_count += 1
      # Logs have hidden newline characters (/n) at the end. .strip() cleans them up.
      clean_line = line.strip()
      print(f"Line {line_count} processed: {clean_line}")

      print("--- Scan Complete ---")
      print(f"Total lines parsed: {line_count}")

except FileNotFoundError:
  print(f"CRITICAL ERROR: {target_file} missing.")
