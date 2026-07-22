from notifypy import Notify

while True:
    notification = Notify()
    notification.title = "Cool Title"
    notification.message = "Even cooler message."
    notification.send()
    