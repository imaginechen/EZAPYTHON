from aip import AipOcr  # pip install baidu-aip
import configparser

class BaiduAPI():
    '''OCR'''

    def __init__(self, filePath):

        # read OCR application password
        target = configparser.ConfigParser()
        target.read(filePath)
        app_id = target.get('baidu_ocr', 'AppID')
        api_key = target.get('baidu_ocr', 'API_Key')
        secret_key = target.get('baidu_ocr', 'Secret_Key')
        
        self.client = AipOcr(app_id, api_key, secret_key)
        

    def picture2Text(self, filePath):
        # read image
        image = self.getPicture(filePath)
        texts = self.client.basicGeneral(image)

        # processing texts
        allTexts = ''
        for word in texts['words_result']:
            allTexts = allTexts + word.get('words','') + '\n'
        return allTexts

    def requestTableRecognition(self, filePath):
        # read image
        image = self.getPicture(filePath)
        texts = self.client.tableRecognitionAsync(image)

        return texts

    def getTableRecognitionResult(self):
        options = {}
        options["result_type"] = "json"
        texts = self.client.getTableRecognitionResult('17667001_1412588', options)

        return texts

    @staticmethod
    def getPicture(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

if __name__ ==  '__main__':
    baiduapi = BaiduAPI('password.ini')
#    print(baiduapi.requestTableRecognition('temp.png'))
    print(baiduapi.getTableRecognitionResult())