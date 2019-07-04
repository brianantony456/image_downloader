from image_downloader import ImageDownloader


if __name__ == '__main__':
    file_urls = 'C:/Users/brian.dsouza/Pictures/image_downloader/fileurls.txt'
    destination_folder = 'C:/Users/brian.dsouza/Pictures/image_downloader/Images'
    image_downloader = ImageDownloader(file_urls=file_urls, destination=destination_folder)
    image_downloader.download_images()
