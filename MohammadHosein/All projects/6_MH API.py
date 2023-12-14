import requests


user_input_name = str(input("Enter your name: "))
user_input_name = user_input_name.replace(" ", "")

gender_api = requests.get(f"https://api.genderize.io/?name={user_input_name}")
nationality_api = requests.get(f"https://api.nationalize.io/?name={user_input_name}")

gender_api = gender_api.json()
nationality_api = nationality_api.json()


gender = gender_api["gender"]
nationality = nationality_api["country"][0]["country_id"]

if gender == "male":
    gender = "M"

elif gender == "female":
    gender = "F"

elif gender != "male" or "female":
    gender = "_"


print()
print(f"Your name gender is: {gender}")
print(f"Your name nationality ID is probably: {nationality}")
