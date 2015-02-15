__author__ = 'renderle'

import logging
import json


from src import restcall
from src.openweather.OpenWeatherParser import OpenWeatherParser

def __evaluateTemp(temp):
    base = 15

    if temp < 0:
        # seems to be very cold
        # we add the negative temp to base -> return value will be lower than base
        return base+temp
    else:
        if temp == 0:
            return base
        else:
            # temp is a positive value
            return base+temp

def __evaluateClouds(cloudFactor):
    base = 100
    # just increase base value with factor
    # very cloudy -> bad value
    # no clouds -> good value ;-)
    return (base - cloudFactor)/2

def __evaluateOverallSituation(overallSituationId):
    base = 10

    idMap = {
        800 : 30,
        801 : 15,
        802 : 5,
        803 : 0,
        804 : -5,
    }

    mappingValue = idMap[overallSituationId]
    return base + mappingValue


def getForecastValue():
    data = restcall.doReq("http://api.openweathermap.org/data/2.5/forecast", "q=Illerrieden,de&units=metric")
    parser = OpenWeatherParser(data)

    # temperature
    temp = parser.getTemperature()
    tempEvaluated = __evaluateTemp(temp)

    # clouds
    cloudFactor = parser.getCloudFactor()
    cloudEvaluated = __evaluateClouds(cloudFactor)

    # overall weather situation
    overallSituationId = parser.getOverallWeatherCondition()
    overallEvaluated = __evaluateOverallSituation(overallSituationId)

    forecastValue = tempEvaluated + cloudEvaluated + overallEvaluated;

    logging.info("")
    logging.info("#######################")
    logging.info("# -_- OpenWeather -_- # ")
    logging.info("#######################")
    logging.info("  temperature:     %s", temp)
    logging.info(" +evalTemp:        %s", tempEvaluated)
    logging.info("  cloudFactor:     %s", cloudFactor)
    logging.info(" +evalCloud:       %s", cloudEvaluated)
    logging.info("  overallSituation:%s", overallSituationId)
    logging.info(" +evalOverallSit:  %s", overallEvaluated)
    logging.info(" overall forecast: %s", forecastValue)
    logging.info("")

    logging.info(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    return forecastValue
