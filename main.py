import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
data = response.json()

def get_tallest_hero(gender: str, has_job: bool):
    import requests

    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    heroes = response.json()

    tallest_hero = None
    max_height = -1

    for hero in heroes:
        # Проверка пола
        if hero.get("appearance", {}).get("gender") != gender:
            continue

        # Проверка наличия работы
        occupation = hero.get("work", {}).get("occupation")
        has_occupation = occupation not in ["-", "", None]

        if has_job != has_occupation:
            continue

        # Получение роста
        height_str = hero.get("appearance", {}).get("height", ["0 cm", "0 cm"])[1]

        if height_str == "0 cm":
            continue

        try:
            height = int(height_str.split()[0])
        except (ValueError, IndexError):
            continue

        # Поиск максимального роста
        if height > max_height:
            max_height = height
            tallest_hero = hero

    if tallest_hero:
        return tallest_hero.get("name")

    return None