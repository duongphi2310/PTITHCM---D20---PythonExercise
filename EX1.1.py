# Write a program to convert minutes into a number of years and days.

# Test Data:
# Input the number of minutes: 3456789
# Expected Output : 6 years, 210 days

phutnam = 60 * 24 * 365
nhap = int(input())
year = nhap // phutnam
day = int((nhap/60/24) % 365)
print(year, "years, ", day, "days")
