__author__ = 'renderle'

import logging
import json

import restcall
from openweather.OpenWeatherParser import OpenWeatherParser

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
        # Thunderstorm
        200 : 15, # thunderstorm with light rain
        201 : 10, #	thunderstorm with rain
        202 :  1, #	thunderstorm with heavy rain
        210 :  5, #	light thunderstorm
        211 :  2, #	thunderstorm
        212 :  0, #	heavy thunderstorm
        221 :  0, #	ragged thunderstorm
        230 :  1, #	thunderstorm with light drizzle
        231 :  0, #	thunderstorm with drizzle
        232 :  0, #	thunderstorm with heavy drizzle

        # Drizzle
        300 : 10 ,# 	light intensity drizzle
        301 :  5,#	drizzle
        302 :  0,# 	heavy intensity drizzle
        310 :  0,# 	light intensity drizzle rain
        311 :  0,#	drizzle rain
        312 :  0,#	heavy intensity drizzle rain
        313 :  0,#	shower rain and drizzle
        314 :  0,#	heavy shower rain and drizzle
        321 :  0,#	shower drizzle

        # Rain
        500 : 10,#	light rain
        501 :  5,#	moderate rain
        502 :  0,#	heavy intensity rain
        503 :  0,#	very heavy rain
        504 :  0,#	extreme rain
        511 :  0,#	freezing rain
        520 :  0,#	light intensity shower rain
        521 :  0,#	shower rain
        522 :  0,#	heavy intensity shower rain
        531 :  0,#	ragged shower rain

        # Snow
        600 :  5,#	light snow
        601 :  0,#	snow
        602 :-10,#	heavy snow
        611 : -5,#	sleet
        612 : -5,#	shower sleet
        615 : -5,#	light rain and snow
        616 : -5,#	rain and snow
        620 : -5,#	light shower snow
        621 : -5,#	shower snow
        622 : -5,#	heavy shower snow

        # Atmosphere
        701 :  0,#	mist
        711 :  0,#	smoke
        721 :  0,#	haze
        731 :  0,#	sand, dust whirls
        741 :  0,#	fog
        751 :  0,#	sand
        761 :  0,#	dust
        762 :  0,#	volcanic ash
        771 :  0,#	squalls
        781 :  0,#	tornado

        # Clouds
        800 : 30, # clear sky
        801 : 15, # few clouds
        802 :  5, #  scattered clouds
        803 :  0, #  broken clouds
        804 : -5, #  overcast clouds

        # Extreme
        900 :  0,#	tornado
        901 :  0,#	tropical storm
        902 :  0,#	hurricane
        903 :  0,#	cold
        904 :  0,#	hot
        905 :  0,#	windy
        906 :  0,#	hail

        # misc
        951 :  0,#	calm
        952 :  0,#	light breeze
        953 :  0,#	gentle breeze
        954 :  0,#	moderate breeze
        955 :  0,#	fresh breeze
        956 :  0,#	strong breeze
        957 :  0,#	high wind, near gale
        958 :  0,#	gale
        959 :  0,#	severe gale
        960 :  0,#	storm
        961 :  0,#	violent storm
        962 :  0#	hurricane

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
    logging.info("#############################################")
    logging.info("#### -_-_-_-_-_- OpenWeather -_-_-_-_-_- #### ")
    logging.info("#############################################")
    logging.info("   temperature:     %s", temp)
    logging.info(" + evalTemp:               %s", tempEvaluated)
    logging.info("   cloudFactor:     %s", cloudFactor)
    logging.info(" + evalCloud:              %s", cloudEvaluated)
    logging.info("   overallSituation:%s", overallSituationId)
    logging.info(" + evalOverallSit:         %s", overallEvaluated)
    logging.info("---------------------------------------------")
    logging.info(" overall forecast:         %s", forecastValue)
    logging.info("")

    logging.info(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    return forecastValue
