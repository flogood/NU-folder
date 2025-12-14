# mapper.py

# ==============================================================================
# 1. IMPORTS AND GLOBAL DATA (The Tools, Rules, and ATT&CK Data)
# ==============================================================================

import json 
from mitreattack.stix20 import MitreAttackData

# --- Load ATT&CK Data ---
# This loads the entire framework data needed for the report.
try:
    print("⏳ Loading MITRE ATT&CK framework data...")
    attack_data = MitreAttackData("enterprise-attack.json")
    print("✅ ATT&CK data loaded successfully.")
except Exception as e:
    print(f"❌ Could not load ATT&CK data: {e}")
    attack_data = None 

# Define the modular rule set (your core threat intelligence)
MAPPING_RULES = {
    # Key: Log Keyword (to look for) -> Value: Technique ID
    "whoami": "T1033",            
    "net user": "T1087.001",      
    "powershell.exe": "T1059.001", 
}


# ==============================================================================
# 2. FUNCTION DEFINITIONS (The Core Logic)
# ==============================================================================

# Function 1: Log Parsing (Develops the robust parsing mechanism)
def parse_logs(file_path):
    """Reads a JSON file and returns the data as a list of Python dictionaries."""
    try:
        with open(file_path, 'r') as f:
            # json.load() converts the raw log text into structured Python data
            log_data = json.load(f)
            print(f"✅ Successfully loaded {len(log_data)} log events.")
            return log_data
    except FileNotFoundError:
        print(f"❌ Error: Log file not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format in log file.")
        return []


# Function 2: ATT&CK Mapping (Transforms raw data into threat intelligence)
def map_event_to_attack(event):
    """Checks a single log event against the MAPPING_RULES dictionary."""
    
    # Safely get the command line and process name, converting to lowercase
    command_line = event.get('CommandLine', '').lower()
    process_image = event.get('Image', '').lower()
    
    # Loop through all the rules
    for keyword, technique_id in MAPPING_RULES.items():
        
        # Check for a match
        if keyword in command_line or keyword in process_image:
            return technique_id
            
    return None 


# Function 3: Get full ATT&CK Details (Needed for the final report visualization)
def get_technique_details(technique_id):
    """Looks up the full name and primary Tactic for a given Technique ID."""
    
    # If the data loading failed, return simple placeholders
    if not attack_data:
        return {"name": technique_id, "tactic": "Unknown"}

    # Use the mitreattack-python library to find the technique object
    technique = attack_data.get_object_by_attack_id(technique_id, "attack-pattern")
    
    if technique:
        name = technique.name
        # Find the Tactic (e.g., 'Discovery', 'Execution')
        kill_chain_phases = getattr(technique, 'kill_chain_phases', [])
        tactic_name = kill_chain_phases[0]['phase_name'].replace('-', ' ').title() if kill_chain_phases else "N/A"
        
        return {
            "name": name, 
            "tactic": tactic_name
        }
    else:
        return {"name": "Technique Not Found", "tactic": "Unknown"}


# ==============================================================================
# 3. MAIN PROGRAM EXECUTION (The Runner)
# ==============================================================================

# 1. Define the input file name
LOG_FILE = 'sample.logs.json'

# 2. Parse the data using Function 1
events = parse_logs(LOG_FILE)

# Dictionary to hold our final findings (counts of techniques found)
mapped_results = {}

if events:
    print("\n--- Starting ATT&CK Mapping ---")
    
    # 3. Loop and Map the events using Function 2
    for event in events:
        
        technique_id = map_event_to_attack(event)
        
        if technique_id:
            # Count the findings (for the summarized report)
            if technique_id not in mapped_results:
                mapped_results[technique_id] = 0
            mapped_results[technique_id] += 1

    # 4. Generate the Final Summarized Report
    print("\n" + "="*70)
    print("                ATT&CK LOG MAPPER: FINAL REPORT")
    print("="*70)
    
    if not mapped_results:
        print("\nNo MITRE ATT&CK Techniques were observed in the logs.")
    
    # The report clearly visualizes the observed attacker behavior (Tactics and Techniques).
    print(f"{'Count':<8}{'Tactic':<20}{'Technique ID':<15}{'Technique Name':<50}")
    print("-" * 100)
    
    # Sort the results by count, prioritizing the most critical findings
    sorted_results = sorted(mapped_results.items(), key=lambda item: item[1], reverse=True)
    
    for tid, count in sorted_results:
        details = get_technique_details(tid)
        
        print(f"{count:<8}{details['tactic']:<20}{tid:<15}{details['name']:<50}")

print("\nProcessing complete. Review the final report above.")