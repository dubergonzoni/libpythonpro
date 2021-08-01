class Sender:
    def send(self, shipper, recipient, subject, body):
        if '@' not in shipper:
            raise InvalidEmail(f'Email de shipper invalid: {shipper}')
        return shipper


class InvalidEmail(Exception):
    pass