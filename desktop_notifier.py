# Show Desktop Notification
# ! pip install plyer

from plyer import notification

def plyer_notification():
     
     notification.notify(
          title = "Plyer Title",               # | Notification Title
          message = "From Plyer Notification", # | Notification Message
          app_name = "TestApp",                # | Name of the App Launching this Notification
          app_icon = None,                     # | Path to the .ico format of icon
          timeout = 5                          # | Time to display the notification in secs. default is 10
     )


if __name__ == '__main__':
     plyer_notification()

