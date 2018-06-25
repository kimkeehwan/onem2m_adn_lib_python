#!/usr/bin/python
import os
import os.path
import configparser

class Config:
    
    def __init__(self):
        self.BaseURL = ""
        self.Origin = ""
        self.PoA = ""

    def loadProperties(self, filepath):
	if 'VCAP_SERVICES' in os.environ:
		import json
		vcap_services = json.loads(os.environ['VCAP_SERVICES'])
		handypia_iot_svc = vcap_services['HandyPIA-IoT-Platform'][0]
		cred = handypia_iot_svc['credentials']
		m2murl = cred['onem2mBaseUrl']
		self.BaseURL = m2murl
		self.PoA = ''
		words = m2murl.split('/')
		self.Origin = words[len(words] - 2 ]
"""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(filepath)

        parser = configparser.RawConfigParser()
        parser.read(filepath)

        self.BaseURL = parser.get('DEFAULT', 'oneM2M_scl_base_url')
        self.Origin = parser.get('DEFAULT', 'oneM2M_scl_base_origin')
        self.PoA = parser.get('DEFAULT', 'oneM2M_poa_url')
"""
        if not self.BaseURL:
            raise ValueError("oneM2M_scl_base_url is empty")
        if not self.Origin:
            raise ValueError("oneM2M_scl_base_origin is empty")


class CONST(object):

    def __setattr__(self, *_):
        pass

    class AdnClz:
        ID = "ADN.ID"
        NAME = "ADN.NAME"

        def __setattr__(self, *_):
            pass

    class CheckClz:
        URI = "CHECK.URI"

        def __setattr__(self, *_):
            pass

    class SensorClz:
        ID = "SENSOR.ID"
        NAME = "SENSOR.NAME"
        HISTORY = "SENSOR.HISTORY"

        def __setattr__(self, *_):
            pass

    class ActuatorClz:
        ID = "ACTUATOR.ID"
        NAME = "ACTUATOR.NAME"
        HISTORY = "ACTUATOR.HISTORY"

        def __setattr__(self, *_):
            pass

    class SensingClz:
        NAME = "SENSING.NAME"
        VALUE = "SENSING.VALUE"

        def __setattr__(self, *_):
            pass

    class ActionClz:
        NAME = "ACTION.NAME"
        VALUE = "ACTION.VALUE"

        def __setattr__(self, *_):
            pass
        
    ID = "ID"
    ADN = AdnClz()
    CHECK = CheckClz()
    SENSOR = SensorClz()
    ACTUATOR = ActuatorClz()
    SENSING = SensingClz()
    ACTION = ActionClz()

CONST = CONST()
