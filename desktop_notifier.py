# Show Desktop Notification
# ! pip install plyer

from plyer import notification

def plyer_notification(title, message, app_name, display_time):
     
     notification.notify(
          title = title,           # | Notification Title
          message = message,       # | Notification Message
          app_name = app_name,     # | Name of the App Launching this Notification
          app_icon = None,         # | Path to the .ico format of icon
          timeout = display_time   # | Time to display the notification in secs. default is 10
     )


if __name__ == '__main__':

     title = "Plyer Title"
     message = "From Plyer Notification"
     app_name = "TestApp"
     display_time = 5

     plyer_notification(title, message, app_name, display_time)

