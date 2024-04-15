from bing_image_downloader import downloader
import os
def download_images():
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))
    print('Downloading images...')

    downloader.download(data, limit=n_images, output_dir="images\\train", adult_filter_off=True, force_replace=False, timeout=60)

saved_folder = input("Enter folder name: ")

def main():
    # if not os.path.exists(saved_folder):
    #     os.mkdir(saved_folder)
    download_images()

main()