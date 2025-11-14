from abc import abstractmethod, ABC
#
# """ Task 1"""
# class PaymentProcessor(ABC):
#     def __init__(self, amount, currency):
#         self.amount = amount
#         self.currency = currency
#     @abstractmethod
#     def process(self,amount):pass
#
# class PayPalProcessor(PaymentProcessor):
#     def process(self,amount):
#         return f"Paypal processed {amount} {self.currency}"
#
# class CardProcessor(PaymentProcessor):
#     def process(self,amount):
#         return f"Card processed {amount} {self.currency}"
# class CryptoPaymentProcessor(PaymentProcessor):
#     def process(self,amount):
#         return f"Crypto processed {amount} {self.currency}"
#
# print(f"\n{PayPalProcessor(100,"USD").process(100)}")
# print(CardProcessor(100,"USD").process(100))
# print(f'{CryptoPaymentProcessor(100,"USD").process(100)} \n')
#
# """ Task 2"""
# class MediaFile(ABC):
#     @abstractmethod
#     def play(self,music): pass
# class MP3File(MediaFile):
#     def play(self,music=None):
#         return f"Playing MP3 file , music name is {music}"
# class WAVFile(MediaFile):
#     def play(self,music=None):
#         return f"Playing WAV file , music name is {music}"
# class MP4File(MediaFile):
#     def play(self,music=None):
#         return f"Playing MP4 file , music name is {music}"
#
# print(MP3File().play("Travis Scoot"))
# print(WAVFile().play("Lana Del Ray"))
# print(f"{MP4File().play("Travis Scoot")}\n")
#
# """ Task 3"""
#
# class NotificationSystem(ABC):
#     @abstractmethod
#     def send(self,message,address):pass
#
# class EmailNotification(NotificationSystem):
#     def send(self,message,address):
#         return f"Email sent: {message} , to {address}"
# class SMSNotification(NotificationSystem):
#     def send(self,message,address):
#         return f"SMS sent: {message} , to {address}"
# class PushNotification(NotificationSystem):
#     def send(self,message,address):
#         return f"Push Notification sent: {message},, to {address}"
#
# print(EmailNotification().send("Hello","example@gmail.com"))
# print(SMSNotification().send("Hello","1234567890"))
# print(PushNotification().send("Hello","Travis Scoot"))