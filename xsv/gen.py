import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("people.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        n = 0
        for i in range(records):
            n += 1
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name

            writer.writerow({
                    "Index" : n,
                    "Phone Number" : fake1.phone_number(),
                    "Job": fake.job().replace(",", "/"),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%a %b %d %H:%m:%d %Z %Y", end_datetime=datetime.date(2000, 1,1)),
                    "Email Id" : userId,
                    })

if __name__ == '__main__':
    records = 1020000
    headers = ["Index", "Phone Number", "Job", "Name", "Birth Date", "Email Id"]
    datagenerate(records, headers)
    print("CSV generation complete!")
