phutnam = 60 * 24 * 365
nhap = int(input())
year = nhap // phutnam
day = int((nhap/60/24) % 365)
print(year, "years, ", day, "days")