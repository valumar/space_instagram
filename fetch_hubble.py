import requests
import os.path

import image_utils


HUBBLE_COLLECTIONS = [
    # "holiday_cards",
    # "wallpaper",
    # "spacecraft",
    # "news",
    # "printshop",
    "stsci_gallery"
]


def fetch_hubble_image(image_id, collection):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    image_url = response.json()['image_files'][-1]['file_url']
    image_utils.get_image(image_url, 'hubble', f'hubble-{collection}-{image_id}{os.path.splitext(image_url)[-1]}')


def get_image_ids_from_hubble_collection(collection):
    url = f'http://hubblesite.org/api/v3/images/{collection}'
    response = requests.get(url)
    image_ids = [image['id'] for image in response.json()]
    return image_ids


def get_all_hubble_images():
    for collection in HUBBLE_COLLECTIONS:
        for image_id in get_image_ids_from_hubble_collection(collection):
            fetch_hubble_image(image_id, collection)


if __name__ == '__main__':
    get_all_hubble_images()
