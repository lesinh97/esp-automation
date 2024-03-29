import machine

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')


rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()