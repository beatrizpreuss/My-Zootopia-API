import requests

API_KEY = 'tX+p7IesWxHN16/NqL2HRg==GrkHAE4JXFrM96K8'
ANIMAL_URL = 'https://api.api-ninjas.com/v1/animals?name='
ANIMAL = 'Fox'

def get_animals_from_api():
    res = requests.get(f'{ANIMAL_URL}{ANIMAL}', headers={'X-Api-Key': API_KEY})
    animals_resp = res.json()
    return animals_resp


def get_html(html_file):
    """ Reads the html file """
    html = open(html_file)
    return html.read()


def get_info():
    """ Gets information about each animal in the json file """
    # animals_data = load_data('animals_resp.json')
    output = ""
    info_from_api = get_animals_from_api()
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
    return output


def replace_info():
    """ Replaces the placeholder in the original html with the
    information about the animals """
    original_html = get_html("animals_template.html")
    animals_info = get_info()
    new_html = original_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    return new_html


def write_html():
    """ Writes a new html file with the replaced information """
    info = replace_info()
    with open("animals.html", "w") as new_html:
        new_html.write(info)


def main():
    write_html()


if __name__ == "__main__":
    main()

