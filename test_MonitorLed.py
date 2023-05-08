
from MonitorLedClassObject import MonitorLed

def test_MonitorLed():
    monitorLed = MonitorLed()
    assert monitorLed.ledText == "ready."
    monitorLed.setFail()
    assert monitorLed.classObject.background_color == "#fb6666"
    assert monitorLed.classObject.color == "white"

if __name__ == "__main__":
    test_MonitorLed()
