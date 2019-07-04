# Python 3.7

import requests
import os
from datetime import datetime


class ImageDownloader:
    """ Class to download images given the destination folder and filename containing image urls """

    def __init__(self, file_urls, destination=""):
        self.destination = destination
        self.file_urls = file_urls

    def download_image(self, url):
        """
        Download one image given the url into the destination folder
        :param url: single url to image
        :return: None
        """
        
        # Request image from url set timeout of 10 seconds
        response = requests.get(url, timeout=10)

        # If response is not ok print download failure
        if not response.ok:
            return "Download Failed"

        # Append timestamp to start of image
        filename_timestamp = datetime.now().strftime("%d_%m_%y_%H.%M.%S.%f") + "_" + (url[url.rfind("/") + 1:])

        # Write the image to the destination folder
        with open(os.path.join(os.path.normpath(self.destination), filename_timestamp), 'wb') as file:
            file.write(response.content)

        return "Download Success"

    def download_images(self):
        """
        Download one image after another from the class instance variable file_urls
        """
        
        try:
            # Read file with image urls
            with open(self.file_urls) as fileHandler:
    
                # Read each url in loop
                for url in fileHandler:
                    # Remove any whitespaces
                    url = url.strip()
                    
                    # Ignore blank lines
                    if not len(url)>0:
                        continue
                        
                    # Download images try except block catches any errors thus resuming download for next link
                    try:
                        # Download image
                        print(self.download_image(url))
                    except Exception as e:
                        print('Error Occurred while downloading the image: ' + str(e))
        except FileNotFoundError as e:
            raise FileNotFoundError("Wrong fileurls path")

