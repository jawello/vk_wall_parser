from user import User


class Group:
    def __init__(self, vk, id):
        self._id = id
        self._members = self.get_group_members(self._id)


