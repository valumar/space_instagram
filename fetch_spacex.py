import requests
import os.path
import image_utils


def get_spacex_list_of_images():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    images = response.json()['links']['flickr_images']
    return images


def fetch_spacex_last_launch():
    for image_number, image_url in enumerate(get_spacex_list_of_images()):
        image_utils.get_image(image_url, 'spacex', f'spacex-{image_number}{os.path.splitext(image_url)[-1]}')


if __name__ == '__main__':
    fetch_spacex_last_launch()
