import unittest
import builtins
from unittest.mock import patch
from image_downloader import ImageDownloader


class TestImageDownloader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        file_urls = 'C:/Users/brian.dsouza/Pictures/image_downloader/fileurls.txt'
        destination_folder = 'C:/Users/brian.dsouza/Pictures/image_downloader/Images'
        self.downloader_1 = ImageDownloader(file_urls=file_urls, destination=destination_folder)
        self.downloader_2 = ImageDownloader(file_urls=file_urls, destination=destination_folder)

    def tearDown(self):
        self.downloader_1 = None
        self.downloader_2 = None

    def test_download_image(self):
        """ Mock download for requests"""
        with patch('image_downloader.requests.get') as mocked_get:

            with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:

                # Mock when return value is True
                mocked_get.return_value.ok = True
                mocked_get.return_value.content = b'imagevalue'
                output1 = self.downloader_1.download_image('http://company.com/image1.png')
                mocked_get.assert_called_with('http://company.com/image1.png', timeout=10)
                self.assertEqual(output1, 'Download Success')

                # Mock when return value is False
                mocked_get.return_value.ok = False
                schedule = self.downloader_2.download_image('http://company.com/image1.png')
                mocked_get.assert_called_with('http://company.com/image1.png', timeout=10)
                self.assertEqual(schedule, 'Download Failed')

    def test_download_images(self):

        with self.assertRaises(FileNotFoundError):
            self.downloader_1.file_urls="wrongurl"
            self.downloader_1.download_images()

if __name__ == '__main__':
    unittest.main()
