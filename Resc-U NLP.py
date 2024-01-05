from datetime import datetime
from fuzzywuzzy import fuzz

Name_Lost = "Elon Musk"
Name_Found = "Elon"

Location_Lost = "Houston, Texas"
Location_Found = "Austin, Texas"

Features_Lost = "Mole on chin, Tall Height"
Features_Found = "Tall Height"

Keywords_Lost = "Intovert, Anxious"
Keywords_Found = "Anxious"

Age_Lost = 14
Age_Found = 16

Gender_Lost = "Female"
Gender_Found = "Male"

Date_Lost = datetime(2024, 1, 22)
Date_Found = datetime(2024, 1, 28)

difference_date = (Date_Found - Date_Lost).days
difference_age = (abs(Age_Found - Age_Lost))

gender_ratio = 0
date_ratio = 0
age_ratio = 0

if Gender_Lost == Gender_Found:
    gender_ratio = 100
else:
    gender_ratio = 0

if difference_age <= 3:
    age_ratio = 100
elif difference_age > 3 and difference_age <= 5:
    age_ratio = 90
elif difference_age > 5 and difference_age <= 7:
    age_ratio = 70
else:
    age_ratio = 0

if difference_date < 10:
    date_ratio = 100
elif difference_date >= 10 and difference_date < 20:
    date_ratio = 90
elif difference_date >= 20 and difference_date < 30:
    date_ratio = 80
elif difference_date >= 30 and difference_date < 60:
    date_ratio = 70
elif difference_date >= 60 and difference_date < 90:
    date_ratio = 60
else:
    date_ratio = 30


name_ratio = fuzz.ratio(Name_Lost, Name_Found)
location_ratio = fuzz.ratio(Location_Lost, Location_Found)
features_ratio = fuzz.ratio(Features_Lost, Features_Found)
keywords_ratio = fuzz.ratio(Keywords_Lost, Keywords_Found)


print(f"Name Match: {name_ratio}%")
print(f"Location Match: {location_ratio}%")
print(f"Features Match: {features_ratio}%")
print(f"Keywords Match: {keywords_ratio}%")
print(f"Date Match: {date_ratio}%")
print(f"Age Match: {age_ratio}%")
print(f"Gender Match: {gender_ratio}%")