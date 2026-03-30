def get_highest_hero(gender: str, has_job: bool):
    import requests

    url = "https://akabab.github.io/superhero-api/api/all.json"
    heroes = requests.get(url).json()

    highest = None
    max_height = 0

    for h in heroes:
        if h["appearance"]["gender"] != gender:
            continue

        occupation = h["work"]["occupation"]
        has_occupation = occupation not in ["-", ""]

        if has_job != has_occupation:
            continue

        height_str = h["appearance"]["height"][1]

        if height_str == "0 cm":
            continue

        height = int(float(height_str.split()[0]))

        if height > max_height:
            max_height = height
            highest = h

    return highest["name"] if highest else None