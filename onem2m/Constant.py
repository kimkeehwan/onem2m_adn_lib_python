
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