class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()
while line != "Stop":
    some_info = line.split()
    sender = some_info[0]
    receiver = some_info[1]
    content = some_info[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

indexes = [int(index) for index in input().split(", ")]
for index in indexes:
    emails[index].send()
for curr_email in emails:
    print(curr_email.get_info())

