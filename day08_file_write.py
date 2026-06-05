# Day 8: File Writing and Appending 

source_file = "sample.log"
report_file = "threat_report.txt"

print(f"--- Starting log scan. Generating report... ---")

try:
  # We open the source to Read ("r") and the report to Append ("a")
  with open(source_file,"r") as infile, open(report_file,"a") as outfile:
    # Write a header for the new scan session
    outfile.write("--- NEW SCAN SESSION ---\n")
    for line in infile:
      clean_line = line.strip()
      # Phase 1 Logic: If we find a failure, write it to the report
      if "FAILED" in clean_line:
        # We must manually add \n to push the next entry to a new line
        outfile.write(clean_line+"\n")
        print(f"THREAT LOGGED: {clean_line}")
      print(f"--- Scan Complete. Check {report_file} for details. ---")

except FileNotFoundError:
  print(f"CRITICAL ERROR: {source_file} missing. Cannot run scan.")
  
