def life_in_weeks(age):
    weeks_left = 52
    total_week_of_life_until_90 = 4680
    year_left = weeks_left * age
    remaining_left_live = total_week_of_life_until_90  - year_left

    print(f"You have {remaining_left_live} weeks left.")


life_in_weeks(56)
