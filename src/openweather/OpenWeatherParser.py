__author__ = 'renderle'


class OpenWeatherParser:
    def __init__(self, data):
        self.data = data

    def getValueFor(self, idx):
        return self.data['list'][idx]

    def getTemperature(self):
        earlymorningValue = self.getValueFor(0)['main']['temp_max']
        morningValue = self.getValueFor(1)['main']['temp_max']
        mixedTemp = (earlymorningValue + 2*morningValue)/3
        return mixedTemp;

    def getCloudFactor(self):
        earlymorningValue = self.getValueFor(0)['clouds']['all']
        morningValue = self.getValueFor(1)['clouds']['all']
        mixedCloudFactor = (earlymorningValue + 3*morningValue)/4
        return mixedCloudFactor

    def getOverallWeatherCondition(self):
        morningValue = self.getValueFor(1)['weather'][0]['id']
        return morningValue

