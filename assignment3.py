# IRCTC Senior Citizen / Special Preference Eligibility

age = int(input("Enter passenger age: "))
gender = input("Enter gender (male/female): ").lower()
traveling_alone = input("Traveling alone? (yes/no): ").lower()
tatkal = input("Is it a Tatkal ticket? (yes/no): ").lower()
blackout_holiday = input("Is journey on a blackout festival holiday? (yes/no): ").lower()

is_senior = age >= 60
is_female_alone = gender == "female" and traveling_alone == "yes"
is_non_tatkal = tatkal == "no"
is_not_blackout = blackout_holiday == "no"

eligible = (is_senior or is_female_alone) and is_non_tatkal and is_not_blackout

print("\n----- Ticket Eligibility -----")
print("Senior Citizen:", is_senior)
print("Female Traveling Alone:", is_female_alone)
print("Non-Tatkal:", is_non_tatkal)
print("Not Blackout Holiday:", is_not_blackout)
print("Eligible:", eligible)
