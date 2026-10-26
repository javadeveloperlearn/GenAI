# strip() -> Removes leading and trailing white spaces
daily_study_target = int(input("Please enter your daily study target: ").strip())

total_week_study_hours = daily_study_target * 7
print("Total Hours: ", total_week_study_hours)