from typing import List, Dict
from datetime import datetime
from user import User
from attachment import Attachment


class Post:
    def __init__(self, user: User, date: datetime, text: str,
                 attachments: List[Attachment], comments: List,
                 likes: List[User]):
        self._user = user
        self._date = date
        self._text = text
        self._attachments = attachments
        self._comments = comments
        self._likes = likes

    def __repr__(self):
        return f'{self.date} {self._user} {text}\n'
