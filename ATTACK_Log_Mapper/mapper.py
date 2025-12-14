# mapper.py

# We need the 'json' tool to read and understand JSON formatted log files.
import json

def parse_logs(file_path):
    """Reads a JSON file and returns the data as a list of Python dictionaries."""
    
    # We use a 'try/except' block to handle errors (like if the file is missing)
    try:
        # 'with open(...)' opens the file for reading ('r')
        with open(file_path, 'r') as f:
            
            # The magic line! json.load() converts the JSON text into a Python list of dictionaries.
            # This makes the data easy for your code to analyze.
            log_data = json.load(f)
            print(f"✅ Successfully loaded {len(log_data)} log events.")
            return log_data
            
    except FileNotFoundError:
        # If we can't find the file, we print an error and return an empty list
        print(f"❌ Error: Log file not found at {file_path}")
        return []
    except json.JSONDecodeError:
        # If the file exists but isn't valid JSON, we catch that error too
        print("❌ Error: Invalid JSON format in log file.")
        return []

# --- Main Program Start ---

# 1. Define the input file name
LOG_FILE = 'sample_logs.json'

# 2. Call the function to parse the data
events = parse_logs(LOG_FILE)

# 3. Check and print the data to see if it worked
if events:
    print("\n--- Example Event Key Data ---")
    
    # We grab the first event to see what information we have
    first_event = events[0]
    
    # In a real security log, we look for key details:
    # We use .get() to safely retrieve data, returning 'N/A' if the key doesn't exist
    print(f"Log Time: {first_event.get('EventTime', 'N/A')}")
    print(f"Process: {first_event.get('Image', 'N/A')}")
    print(f"Command: {first_event.get('CommandLine', 'N/A')}")
    
    # This step is critical because it tells you exactly what data you have to map!