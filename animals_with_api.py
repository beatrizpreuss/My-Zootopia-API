import requests
from numpy.ma.core import empty

API_KEY = 'tX+p7IesWxHN16/NqL2HRg==GrkHAE4JXFrM96K8'
ANIMAL_URL = 'https://api.api-ninjas.com/v1/animals?name='


def get_user_input():
    user_animal = input("Enter a name of an animal: ")
    return user_animal


def get_animals_from_api(user_animal):
    res = requests.get(f'{ANIMAL_URL}{user_animal}', headers={'X-Api-Key': API_KEY})
    animals_resp = res.json()
    return animals_resp


def get_html(html_file):
    """ Reads the html file """
    html = open(html_file)
    return html.read()


def get_info(user_animal):
    """ Gets information about each animal in the json file """
    # animals_data = load_data('animals_resp.json')
    output = ""
    info_from_api = get_animals_from_api(user_animal)
    for animal in info_from_api:
        try:
            output += (f'<li class="cards__item">'
                       f'<div class="card__title">{animal["name"]}</div>\n'
                       f'<div class="card__text">'
                       f"<ul>"
                       f"<li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n"
                       f"<li><strong>Location:</strong> {animal["locations"][0]}</li>\n"
                       f"<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n"
                       f"</ul>"
                       f"</div>"
                       f"</li>")
        except KeyError:
            continue
    if output == "":
        output += f"<h2 text-align: center>The animal {user_animal} doesn't exist.<h2>"
    return output


def replace_info(user_animal):
    """ Replaces the placeholder in the original html with the
    information about the animals """
    original_html = get_html("animals_template.html")
    animals_info = get_info(user_animal)
    new_html = original_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    return new_html


def write_html(user_animal):
    """ Writes a new html file with the replaced information """
    info = replace_info(user_animal)
    with open("animals.html", "w") as new_html:
        new_html.write(info)


def main():
    user_animal = get_user_input()
    write_html(user_animal)
    print("Website was successfully generated to the file animals.html")


if __name__ == "__main__":
    main()

