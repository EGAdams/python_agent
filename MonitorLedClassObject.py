
class MonitorLedClassObject:
    def __init__(self):
        self.background_color = None
        self.color = None

class MonitorLed:
    classObject = None
    ledText = None
    RUNNING_COLOR = None
    PASS_COLOR = None
    FAIL_COLOR = None

    def __init__(self):
        self.classObject = MonitorLedClassObject()
        self.ledText = "ready."
        self.RUNNING_COLOR = "lightyellow"
        self.PASS_COLOR = "lightgreen"
        self.FAIL_COLOR = "#fb6666" # lightred is not understood by CSS.  Whaaa... ??

    def setFail(self):
        self.setLedBackgroundColor(self.FAIL_COLOR)
        self.setLedTextColor("white")

    def setLedBackgroundColor(self, newColor):
        self.classObject.background_color = newColor

    def setLedTextColor(self, newColor):
        self.classObject.color = newColor

    def setLedText(self, newText):
        self.ledText = newText
