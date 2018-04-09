from onem2m import AE, Constant

cli = AE.ClientLib()

arg = {Constant.CONST.ADN.ID:'S111115', Constant.CONST.ADN.NAME:'S111115', Constant.CONST.CHECK.URI:"S111115",
    Constant.CONST.SENSOR.ID:'111111', Constant.CONST.SENSOR.NAME:'Temp', Constant.CONST.SENSOR.HISTORY:11}

arg1 = {Constant.CONST.ADN.ID:'S111115', Constant.CONST.SENSOR.ID:'111111',Constant.CONST.SENSOR.NAME:'Temp',
    Constant.CONST.SENSING.NAME:'R1',Constant.CONST.SENSING.VALUE:32}

arg2 = {Constant.CONST.ADN.ID:'S111115',Constant.CONST.ID:'111111'}

print(cli.checkDuplicated(arg))

print(cli.createADN(arg))

print(cli.registrySensor(arg))

print(cli.sendSensingReport(arg1))

print(cli.getLastValue(arg2))

print(cli.getValues(arg2))

print(cli.getADNAll())