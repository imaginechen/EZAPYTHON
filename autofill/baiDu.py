from aip import AipOcr
import configparser

class BaiDuAPI():
    """baidu OCR"""
    def __init__(self, filePath):
        target = configparser.ConfigParser()
        target.read(filePath)
        APP_ID = target.get('myPW', 'APP_ID')
        API_KEY = target.get('myPW', 'API_KEY')
        SECRET_KEY = target.get('myPW', 'SECRET_KEY')

        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        print(APP_ID)
        print(API_KEY)
        print(SECRET_KEY)

    def picture2text(self, filePath):
        image = self.getPicture(filePath)
        text = self.client.basicAccurate(image)
        print(text)

    #@staticmethod
    def getPicture(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

baiduapi = BaiDuAPI('passwd.ini')
baiduapi.picture2text('P1.JPG')
