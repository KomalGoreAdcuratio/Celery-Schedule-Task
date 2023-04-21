# Email-Sending-Via-Django
https://www.youtube.com/watch?v=gOr-RQcfjMQ
https://docs.djangoproject.com/en/4.2/topics/email/

from django.core.mail import send_mail


send_mail(
    "Subject here",
    "Here is the message.",
    "from@example.com",
    ["to@example.com"],
    fail_silently=False,
)

EX :
send_mail(
    "Subject",
    "Message.",
    "from@example.com",
    ["john@example.com", "jane@example.com"],
)


message1 = (
    "Subject here",
    "Here is the message",
    "from@example.com",
    ["first@example.com", "other@example.com"],
)
message2 = (
    "Another Subject",
    "Here is another message",
    "from@example.com",
    ["second@test.com"],
)
send_mass_mail((message1, message2), fail_silently=False)

Ex:
datatuple = (
    ("Subject", "Message.", "from@example.com", ["john@example.com"]),
    ("Subject", "Message.", "from@example.com", ["jane@example.com"]),
)
send_mass_mail(datatuple)

send_mass_mail() vs. send_mail()

The main difference between send_mass_mail() and send_mail() is that send_mail() opens a connection to the mail server each time it’s executed, while send_mass_mail() uses a single connection for all of its messages. This makes send_mass_mail() slightly more efficient.# Celery-Schedule-Task
