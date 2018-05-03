import vk_api
from user import User


class VK:
    def __init__(self, login, password):
        self._vk_session = vk_api.VkApi(login, password)

        try:
            self._vk_session.auth()
        except vk_api.AuthError as error_msg:
            print(error_msg)

        self._tools = vk_api.VkTools(self._vk_session)
        self._pool = vk_api.VkRequestsPool(self._vk_session)

    def get_current_user(self):
        return self._pool.method('users.get')

    def get_group(self, group_id):
        group = self._pool.method(
            'groups.getById',  # Метод
            {'group_id': group_id, 'fields': ['description', 'start_date']}
        )
        return group

    def get_group_members(self, group_id):
        members = self._tools.get_all('groups.getMembers', max_count=1000,
                                      values=dict(group_id=group_id, fields=['first_name', 'last_name'])
                                      )
        result = {-group_id: {'first_name': 'Кабань', 'last_name': '&Ко'}}
        for i in members:
            result[i[id]] = User(**i)
        return members

