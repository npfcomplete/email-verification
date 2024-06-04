import sys
import datetime

csv_columns = ["First Name", "Middle Initial", "Surname", "Gender", "Street Address", "City", "State", "Zipcode", "Age", "Birthday", "Username", "Occupation", "Company", "Vehicle"]

def get_info(website, index):
    with open ("names.csv", "r") as csv_file:
        lines = csv_file.readlines()
        info = lines[index]
        
        file_name = str(datetime.date.today()) + "-" + website + ".csv"
        output_file = open(file_name, "w")
        output_file.write(info)

    
        info = info.split(",")
        i = 0
        while i < len(csv_columns):
            print(csv_columns[i] + ": " + info[i]) 
            i += 1

def main():
    if len(sys.argv) != 3:
        print("Don't forget the website!: python3 <> <website_name> <index>")
        exit(1)
        
    website = sys.argv[1]
    index = int(sys.argv[2])
    get_info(website, index)

if __name__ == "__main__":
    main()
