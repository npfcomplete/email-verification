import subprocess
from subprocess import PIPE
import json
import sys
import datetime

def call_api():
    command = "curl https://api.namefake.com/united-states"

    process = subprocess.Popen(
        command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )

    std_out, std_err = process.communicate()

    return std_out
    

def main():
    # Check args before to prevent issues
    if len(sys.argv) != 2:
        print("Forgot arguments: python3 name_generator.py <output_file>") 
        exit(1)

    # Get json values
    json_val = call_api()
    load_json = json.loads(json_val)
    parsed_json = json.dumps(load_json, indent = 4)
    
    # YYYY-MM-DD-url.json
    date = str(datetime.date.today())
    file_name = date + "-" + sys.argv[1] + ".json"

    # Output json to file for later
    with open(file_name, "w") as file:
        file.write(parsed_json)

    for key, value in load_json.items():
        if key == "name":
            print(f"{key}: {value}")
        elif key == "birth_data":
            print(f"{key}: {value}")
        elif key == "address":
            print(f"{key}: {value}")
        elif key == "username":
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
