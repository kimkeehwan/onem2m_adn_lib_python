from onem2m import Config, Constant
import string
import random
import json
import requests
import base64
from datetime import datetime

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class ClientLib:
    conf = Config.Config()

    def __init__(self):
        self.conf.loadProperties("oneM2M.conf")
        pass

    def createADN(self, args): 
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putResourceType('2')
        headers.putOrigin(args[Constant.CONST.ADN.ID])

        body = {"m2m:ae": {"api":"", "rr":False, "lbl":args[Constant.CONST.ADN.NAME],"apn":args[Constant.CONST.ADN.ID], "poa": self.conf.PoA}}

        str = json.dumps(body)

        res = requests.post(self.conf.BaseURL, headers=headers.content, data=str)

        return res.status_code

    def checkDuplicated(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(self.conf.Origin)

        url = self.conf.BaseURL + "/" + args[Constant.CONST.CHECK.URI]

        res = requests.get(url, params={"rcn":5}, headers=headers.content )

        return res.status_code
    
    def registrySensor(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putResourceType('3')
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        headers.putNm(args[Constant.CONST.SENSOR.NAME])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID]

        body = {"m2m:cnt": {"rn":args[Constant.CONST.SENSOR.ID], "lbl":args[Constant.CONST.SENSOR.NAME],"mni":args[Constant.CONST.SENSOR.HISTORY]}}

        str = json.dumps(body)
        res = requests.post(url, headers=headers.content, data=str)
        
        return res.status_code

    def updateSensor(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.SENSOR.ID]

        body = {"m2m:cnt": {"lbl":args[Constant.CONST.SENSOR.NAME],"mni":args[Constant.CONST.SENSOR.HISTORY]}}

        str = json.dumps(body)
        res = requests.put(url, headers=headers.content, data=str)

        return res.status_code

    def deleteSensor(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.SENSOR.ID]

        res = requests.delete(url, headers=headers.content)

        return res.status_code

    def registryActuator(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putResourceType('3')
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        headers.putNm(args[Constant.CONST.ACTUATOR.NAME])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID]

        body = {"m2m:cnt": {"rn":args[Constant.CONST.ACTUATOR.ID], "lbl":args[Constant.CONST.ACTUATOR.NAME],"mni":args[Constant.CONST.ACTUATOR.HISTORY]}}

        str = json.dumps(body)
        res = requests.post(url, headers=headers.content, data=str)
        
        return res.status_code

    def updateActuator(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.ACTUATOR.ID]

        body = {"m2m:cnt": {"lbl":args[Constant.CONST.ACTUATOR.NAME],"mni":args[Constant.CONST.ACTUATOR.HISTORY]}}

        str = json.dumps(body)
        res = requests.put(url, headers=headers.content, data=str)

        return res.status_code

    def deleteActuator(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.ACTUATOR.ID]

        res = requests.delete(url, headers=headers.content)

        return res.status_code

    def sendSensingReport(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putResourceType('4')
        headers.putOrigin(args[Constant.CONST.ADN.ID])
       
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.SENSOR.ID] + "?rcn=0"
        

        innerbody = {"thingId":args[Constant.CONST.ADN.ID], "time": datetime.now().strftime("%Y%m%d%H%M%S"), "resourceId":args[Constant.CONST.SENSING.NAME],
            "value": {args[Constant.CONST.SENSING.NAME]:args[Constant.CONST.SENSING.VALUE]}}

        innerbodystr = json.dumps(innerbody)
        encoded = base64.b64encode(innerbodystr.encode('ascii'))

        body = {"m2m:cin": {"lbl":"sensing value report" + args[Constant.CONST.SENSOR.NAME],
             "cnt":"application/json:1", "con":encoded.decode("utf-8") }}

        str = json.dumps(body)
        res = requests.post(url, headers=headers.content, data=str)
        
        return res.status_code
        
    def sendActuatorResult(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putResourceType('4')
        headers.putOrigin(args[Constant.CONST.ADN.ID])
       
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.ACTUATOR.ID] + "?rcn=0"
        
        innerbody = {"thingId":args[Constant.CONST.ADN.ID], "time": datetime.now().strftime("%Y%m%d%H%M%S"), "resourceId":args[Constant.CONST.SENSING.NAME],
            "value": {args[Constant.CONST.ACTION.NAME]:args[Constant.CONST.ACTION.VALUE]}}

        innerbodystr = json.dumps(innerbody)
        encoded = base64.b64encode(innerbodystr.encode('ascii'))

        body = {"m2m:cin": {"lbl":"sensing value report" + args[Constant.CONST.ACTUATOR.NAME],
             "cnt":"application/json:0", "con":innerbodystr }}

        str = json.dumps(body)
        res = requests.post(url, headers=headers.content, data=str)
        
        return res.status_code

    def getLastValue(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.ID] + "/la"

        res = requests.get(url, headers=headers.content)        
        obj = json.loads(res.content)
        return json.loads(base64.b64decode(obj["m2m:cin"]["con"]))
 
    def getValues(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])
        
        values = []
        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.ID] + "?rcn=5"
        res = requests.get(url, headers=headers.content)
        if not res.status_code == 200:
            return values
        
        res = requests.get(url, headers=headers.content)        
        obj = json.loads(res.content)
        children = obj["m2m:cnt"]["ch"]
        for ele in children:
            childurl = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID] + "/" + args[Constant.CONST.ID] + "/" + ele["nm"]
            childres = requests.get(childurl, headers=headers.content)
            if childres.status_code == 200:
                valueJson = json.loads(childres.content)
                values.append(json.loads(base64.b64decode(valueJson["m2m:cin"]["con"])))

        return values

    def getDevice(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])

        url = self.conf.BaseURL + "/" + args[Constant.CONST.CHECK.URI]

        res = requests.get(url, params={"rcn":5}, headers=headers.content )
        if not res.status_code == 200:
            return
        return json.loads(res.content)

    def getDeviceAll(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])

        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID]

        res = requests.get(url, params={"rcn":5}, headers=headers.content )
        if not res.status_code == 200:
            return
        return json.loads(res.content)
        
    def sendActuation(self, args):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(args[Constant.CONST.ADN.ID])

        url = self.conf.BaseURL + "/" + args[Constant.CONST.ADN.ID]

        body = {"id":args[Constant.CONST.ACTUATOR.ID], "value":args[Constant.CONST.ACTUATOR.VALUE]}

        str = json.dumps(body)
        res = requests.post(url, headers=headers.content, data=str)
    
        return res.status_code

    def getADNAll(self):
        headers = self.HttpHeaders()
        headers.putRequestId(id_generator())
        headers.putOrigin(self.conf.Origin)
        
        url = self.conf.BaseURL

        res = requests.get(url, params={"rcn":5}, headers=headers.content )
        if not res.status_code == 200:
            return
        jsonObj = json.loads(res.content)
        return jsonObj["m2m:cb"]["ch"]

    class HttpHeaders:
        
        def __init__(self):
            self.content = {'content-type':'application/json', 'Accept':'application/json'}
            pass

        def putResourceType(self, rt):
            self.content['content-type'] = 'application/json;ty=' + rt 
        
        def putOrigin(self, origin):
            self.content['X-M2M-Origin'] = origin
            pass

        def putRequestId(self, rid):
            self.content['X-M2M-RI'] = rid
        
        def putNm(self, nm):
            self.content['X-M2M-NM'] = nm
