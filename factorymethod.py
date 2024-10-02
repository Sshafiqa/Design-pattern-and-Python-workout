from abc import ABC, abstractmethod


# Step 1: Define the base Notification interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


# Step 2: Create concrete notification classes
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending Email: {message}")


class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending Push Notification: {message}")


# Step 3: Create the NotificationFactory
class NotificationFactory:
    @staticmethod
    def get_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")


# Step 4: Client code using the factory
if __name__ == "__main__":
    notification_type = input("Enter notification type (email, sms, push): ").lower()

    factory = NotificationFactory()

    # Create notification based on the user input
    try:
        notification = factory.get_notification(notification_type)
        message = input("Enter the message to send: ")
        notification.send(message)
    except ValueError as e:
        print(e)
