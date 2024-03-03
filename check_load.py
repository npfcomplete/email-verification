from subprocess import PIPE
import subprocess
import sys
import csv
import datetime
import re

command = 'wget --referer="https://www.google.com" \
           --user-agent="Mozilla/5.0 (Windows; U; Windows NT5.1; en-US; rv:1.8.1.6) \
           Gecko/20070725 Firefox/2.0.0.6" \
           --header="Accept: text/xml,application/xml,\
           application/xhtml+xml,text/html;q=0.9,text/plain;1=0.8,image/png,\
           */*;q=0.5" \
           --header="Accept-Language: en-us,en;q=0.5" \
           --header="Accept_encoding: gzip,deflate" \
           --header="Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7" \
           --header="Keep-Alive: 300" -dnv --spider' 


cmd = '--header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" \
       --header="Accept-Encoding: gzip,deflare,br" \
       --user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" \
       --referer="https://www.google.com" \
       --header="Accept-Language: en-us,en;q=0.5" -dnv --spider '

def process_file(csv_path, load_file_path, fail_file_path):
    load_list = ""
    fail_list = ""
    date = str(datetime.date.today())

    with open(csv_path, "r") as file:
        print("Opened file {csv_path}", csv_path)
        for line in file:
            new_entry = ""
            split_line = line.split(",")
            rank = split_line[0]
            url = split_line[1]
            resulting_load = run_wget(url)
            new_entry = "{},{},{},{}".format(rank, url, resulting_load, date)

            # Website loads
            if (resulting_load[0] == "2"):
                load_list += new_entry
            else:
                fail_list += new_entry

    fsuccess = open(load_file_path, "w")
    ffail = open(fail_file_path, "w")

    fsuccess.write(load_list)
    ffail.write(fail_list)

    fsuccess.close()
    ffail.close()


def run_wget(url):    
    ok_response = "400" 
    index = 0

    process = subprocess.Popen(
        command + url, 
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_err, std_out = process.communicate()

    pattern = "(---response begin---.*)([0-9]{3})"
    matches = re.findall(pattern, std_out)     
    try:
        ok_response = (matches[len(matches)-1])[1]
    except:
        print(std_out)

    return ok_response


def main():
    if len(sys.argv) != 4:
        print(sys.argv)
        print("Forgot arguments: python3 <> <input_file> <success_file> <fail_file>")
        exit(1)

    process_file(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
