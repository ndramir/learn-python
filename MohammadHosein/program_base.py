import requests
import Country


def probability_nationality(probability):
    if probability < 1:
        probability = str(probability)
        probability = probability.replace(".", "")
        probability = probability[1:3]
        probability = int(probability)

    elif probability == 1:
        probability = 100

    return probability


print()

user_input_name = str(input("Please enter your name: "))
user_input_name = user_input_name.replace(" ", "")

gender_api = requests.get(f"https://api.genderize.io/?name={user_input_name}")
nationality_api = requests.get(f"https://api.nationalize.io/?name={user_input_name}")

gender_api = gender_api.json()
nationality_api = nationality_api.json()


gender = gender_api["gender"]

if gender == "male":
    gender = "M"


elif gender == "female":
    gender = "F"

elif gender != "male" or "female":
    gender = "_"


nationality_1st_id = nationality_api["country"][0]["country_id"]
nationality_1st_country = Country.country_id_list[nationality_1st_id]
nationality_1st_chance = probability_nationality(
    nationality_api["country"][0]["probability"]
)

if nationality_1st_chance < 100:
    nationality_2nd_id = nationality_api["country"][1]["country_id"]
    nationality_2nd_country = Country.country_id_list[nationality_2nd_id]
    nationality_2nd_chance = probability_nationality(
        nationality_api["country"][1]["probability"]
    )

if nationality_1st_chance < 100:
    nationality_3rd_id = nationality_api["country"][2]["country_id"]
    nationality_3rd_country = Country.country_id_list[nationality_3rd_id]
    nationality_3rd_chance = probability_nationality(
        nationality_api["country"][2]["probability"]
    )


print()
print()

print(f"Your name gender is: {gender}")
print()
print(f"Your are {nationality_1st_chance}% from the country: {nationality_1st_country}")

if nationality_1st_chance < 100 and nationality_2nd_chance > 0:
    print(
        f"Your are {nationality_2nd_chance}% from the country: {nationality_2nd_country}"
    )

if nationality_1st_chance < 100 and nationality_3rd_chance > 0:
    print(
        f"Your are {nationality_3rd_chance}% from the country: {nationality_3rd_country}"
    )


print()
