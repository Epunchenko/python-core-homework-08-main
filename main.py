from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    week_days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",
        6: "Monday",
    }
    d1 = date.today()
    next_week = timedelta(days=7)
   # work_week = timedelta(days=5)
    d2 = d1 + next_week
   # d3 = d1 + work_week

   # print(work_week)

    dictionary = {}

    if not users:
        return dictionary

    for user in users:
        for val in user.values():
            if isinstance(val, str):
                first_name = val.split(" ")[0]
                # print(first_name)
            else:
                birth_day = datetime(d1.year, val.month, val.day).date()
                day = birth_day.weekday()
                week_day = week_days[day]
                # print(week_day)

                if d1 <= birth_day < d2:
                    dictionary.setdefault(week_day, [])
                    dictionary[week_day].append(first_name)
                if d1.month == 12 and birth_day.month == 1 and d1.day > 24:
                    dictionary.setdefault(week_day, [])
                    dictionary[week_day].append(first_name)

    return dictionary


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1965, 11, 15).date()},
        {"name": "Sarah Connor", "birthday": datetime(1965, 11, 17).date()},
        {"name": "Dan Balan", "birthday": datetime(1979, 11, 13).date()},
        {"name": "John Starks", "birthday": datetime(1955, 11, 12).date()},
        {"name": "Jenifer Aniston", "birthday": datetime(1969, 11, 14).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
