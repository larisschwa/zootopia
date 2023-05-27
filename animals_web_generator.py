import data_fetcher


def serialize_animal(animal_obj):
    """Serialize animal info"""
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj["name"]}</div><br/>\n'
    output += '<p class="card__text">'
    output += f'<strong>Diet:</strong> ' \
              f'{animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> ' \
              f'{animal_obj["locations"][0]}<br/>\n'
    if "type" in animal_obj['characteristics']:
        output += f'<strong>Type:</strong> ' \
                  f'{animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>'
    output += '</li>'
    return output


def generate_website(animal):
    """Generates the website"""
    data = data_fetcher.fetch_data(animal)
    if data:
        output = ''
        for animal_obj in data:
            try:
                output += serialize_animal(animal_obj)
            except KeyError:
                pass

        with open("animals_template.html", "r") as fileobj:
            old_path = fileobj.read()

        old_txt = "__REPLACE_ANIMALS_INFO__"
        new_txt = output

        with open("animals.html", "w") as new_file:
            new_path = old_path.replace(old_txt, new_txt)
            new_file.write(new_path)
    else:
        with open("animals_template.html", "r") as fileobj:
            old_path = fileobj.read()

        old_txt = "__REPLACE_ANIMALS_INFO__"
        new_txt = f'<h2>The animal "{animal}" doesn\'t exist.</h2>'

        with open("animals.html", "w") as new_file:
            new_path = old_path.replace(old_txt, new_txt)
            new_file.write(new_path)


def main():
    animal = input("Enter the name of an animal: ")
    generate_website(animal)


if __name__ == '__main__':
    main()
