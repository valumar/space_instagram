import os
import time
import image_utils

from instabot import Bot
from dotenv import load_dotenv
load_dotenv()


INSTA_LOGIN = os.getenv("INSTA_LOGIN")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")


def upload_photo(image):
    bot = Bot()
    bot.login(username=INSTA_LOGIN, password=INSTA_PASSWORD)
    bot.upload_photo(image)


def remove_garbage():
    images = image_utils.get_list_of_images()
    garbage_files =['blacklist', 'comments', 'followed', 'friends', 'skipped', 'unfollowed', 'whitelist']
    for file in garbage_files:
        try:
            print(f'Removing \"{file}.txt\"')
            os.remove(f'{file}.txt')
        except FileNotFoundError:
            pass
    for image in images:
        if image.find('CONVERTED') > 0:
            print(f'Removing \"{image}\"')
            os.remove(image)
    print('All garbage removed')


if __name__ == '__main__':
    remove_garbage()
    pause = 60
    try:
        with open('posted_pics.txt', 'r', encoding='utf8') as f:
            posted_pic_list = f.read().splitlines()
    except Exception:
        posted_pic_list = []
    images = image_utils.get_list_of_images()
    print(posted_pic_list)
    for image in images:
        if image not in posted_pic_list:
            upload_photo(image)
            posted_pic_list.append(image)
            with open('posted_pics.txt', 'a', encoding='utf8') as f:
                f.write(image + "\n")
            time.sleep(pause)
    remove_garbage()
