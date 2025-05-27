import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_html(html_file):
    """ Reads the html file """
    html = open(html_file)
    return html.read()


def get_info():
    """ Gets information about each animal in the json file """
    animals_data = load_data('animals_data.json')
    output = ""
    for animal in animals_data:
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