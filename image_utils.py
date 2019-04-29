import logging
import pathlib
import os.path
import requests

IMAGE_FOLDER = 'images'

logging.basicConfig(
    format='%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.DEBUG,
    filename='log.log'
)


def get_image(url, api_name, filename):
    pathlib.Path(
        os.path.join(IMAGE_FOLDER, api_name)
    ).mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    logging.info(f'Getting image: {os.path.join(IMAGE_FOLDER, api_name, filename)}')
    with open(os.path.join(IMAGE_FOLDER, api_name, filename), 'wb') as file:
        file.write(response.content)


def get_list_of_images():
    images = []
    for root, subs, files in os.walk(IMAGE_FOLDER):
        for file in files:
            images.append(os.path.join(root, file))
        for folder in subs[:]:
            if folder.startswith('.'):
                subs.remove(folder)
    return images


if __name__ == '__main__':
    pass
