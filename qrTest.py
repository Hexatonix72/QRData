import json

import qrcode

import datetime

StartTimeInt = datetime.datetime.now()
EndTimeInt = datetime.timedelta(seconds=20)
start_time = str(StartTimeInt)
end_time = str(StartTimeInt + EndTimeInt)


class QRData:
    def __init__(self, StartTime, DeviceID, EndTime):
        self.StartTime = StartTime
        self.DeviceID = DeviceID
        self.EndTime = EndTime


def to_json(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__)


QR1 = QRData(start_time, 0, end_time)

QR = to_json(QR1)
img = qrcode.make(QR)
type(img)  # qrcode.image.pil.PilImage
img.save("test_file.png")
