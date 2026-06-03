# Day 6: File Handling - Reading Data

target_file = "sample.log"

print(f"--- Attempting to open: {target_file} ---")

# 'r' stands for read mode.
#'try/except' prevents the script from exploding if the file os missing.
try:
  with open(target_file,"r") as file:
    # .read() grabs the entire file as one giant string 
    contents = file.read()
    print("--- File Contents Below ---")
    print(contents)

except FileNotFoundError:
  print(f"CRITICAL ERROR: {target_file} does not exist in this directory.")
  
