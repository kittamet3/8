def Turn_Right():
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 120)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.servo_run(maqueen.Servos.S1, 40)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 95)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(1000)
def Turn_Left():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 120)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.servo_run(maqueen.Servos.S1, 40)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 95)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(1000)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_COLOR_RECOGNITION)
maqueen.servo_run(maqueen.Servos.S1, 40)

def on_forever():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK) or huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        maqueen.servo_run(maqueen.Servos.S1, 120)
        basic.pause(200)
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        Turn_Left()
    if huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        Turn_Right()
basic.forever(on_forever)
