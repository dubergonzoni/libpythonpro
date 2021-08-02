class SpamSender:
    def __init__(self, session, sender):
        self.session = session
        self.sender = sender

    def send_emails(self, shipper, subject, body):
        for user in self.session.list():
            self.sender.send(
                shipper,
                user.email,
                subject,
                body
            )