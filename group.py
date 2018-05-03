from user import User


class Group:
    def __init__(self, vk, id):
        self._vk = vk
        self._id = id
        self._members = self._parse_group_members(self._vk.get_group_members(self._id))

    def _parse_group_members(self, members):
        group = self._vk.get_group(self._id)
        result = {-self._id: {'first_name': group['name']}}
        for i in members:
            result[i[id]] = User(**i)
        return result



