from subprocess import PIPE
import subprocess
import sys
import csv
import datetime
import re

def process_file(csv_path, success_file_path, fail_file_path):
    success_output = ""
    fail_output = ""

    with open(csv_path, "r") as file:
        for line in file:
            split_line = line.split(",")
            rank = split_line[0]
            url = split_line[1]

            resultingLoad = run_wget(url)

            # Website loads
            if (resultingLoad == "200"):
                success_output += rank + "," + url + "," + resultingLoad + "," + str(datetime.date.today())
            else:
                fail_output += rank + "," + url + "," + resultingLoad + "," + str(datetime.date.today())

    fsuccess = open(success_file_path, "w")
    ffail = open(fail_file_path, "w")

    fsuccess.write(success_output)
    ffail.write(fail_output)

    fsuccess.close()
    ffail.close()


def run_wget(url):
    ok_response = "400" # default for now, is there always a response code?
    index = 0

    process = subprocess.Popen(
        "wget --spider " + url, # spider prevents download
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_err, std_out = process.communicate()
    
    pattern = "(HTTP request sent, .+)([0-9]{3})"
    matches = re.findall(pattern, string)     
    ok_response = (matches[len(matches)-1])[1]

    return ok_reponse


def main():
    if len(sys.argv) != 4:
        print(sys.argv)
        print("Forgot arguments: python3 <> <input_file> <success_file> <fail_file>")
        exit(1)

    print("ran\n\n\n")

    counter = 0
    for arg in sys.argv:
        print("Arg " + str(counter) + ":" + arg)
        counter += 1

    process_file(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
