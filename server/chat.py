"""
Represents and stores information about the chat
"""


class Chat(object):

    def __init__(self, r):
        self.content = []
        self.round = r

    def update_chat(self, msg):
        self.content.append(msg)
        if len(self.content) > 35:
            del self.content[0]

    def get_chat(self):
        return self.content

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return "".join(self.content)

    def __repr__(self):
        return str(self)
