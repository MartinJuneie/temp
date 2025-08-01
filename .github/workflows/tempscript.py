# .github/workflows/scripts/tempscript.py

import csv

def main():
    filename = "sample.csv"

    # Dummy data
    headers = ["Name", "Age"]
    rows = [
        {"Name": "AK", "Age": 30},
        {"Name": "Martin", "Age": 25},
        {"Name": "Lee", "Age": 40}
    ]

    # Write CSV file
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
