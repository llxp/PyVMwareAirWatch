from .system import System


class UserGroups(System):
    """
    A class to manage all core functionalities for AirWatch User Groups.
    """

    def __init__(self, client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """Returns the Users Groups matching the search parameters."""
        response = System._get(self, path='/usergroups/search', params=kwargs)
        return response

    def search_users(self, id, **kwargs):
        """Retrieves list of users from the provided user group id."""
        _path = '/usergroups/{}/users'.format(id)
        response = System._get(self, path=_path, params=kwargs)
        return response

    def create_group(self, group_data):
        """Create a custom user group."""
        _path = '/usergroups/createcustomusergroup'
        response = System._post(self, path=_path, data=group_data)
        return response

    def add_user_to_group(self, groupid, userid):
        """Create a custom user group."""
        _path = '/usergroups/{}/user/{}/addusertogroup'.format(groupid, userid)
        response = System._post(self, path=_path)
        return response

    def remove_user_from_group(self, groupid, userid):
        """Create a custom user group."""
        _path = '/usergroups/{}/user/{}/removeuserfromgroup'.format(groupid, userid)
        response = System._post(self, path=_path)
        return response
