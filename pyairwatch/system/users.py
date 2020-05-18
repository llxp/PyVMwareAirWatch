from .system import System


class Users(System):

    def __init__(self, client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Enrollment User's details matching the search parameters

        /api/system/users/search?{params}

        PARAMS:
            username={username}
            firstname={firstname}
            lastname={lastname}
            email={email}
            organizationgroupid={locationgroupid}
            role={role}
        """
        return System._get(self, path='/users/search', params=kwargs)

    def delete_user_by_id(self, user_id):
        """
        Delete the enrollment user by enrollment user id

        :param user_id:
        :return: API response
        """
        path = '/users/{}/delete'.format(user_id)
        return System._delete(self, path=path)

    def create_device_registration_to_user(self, user_id, register_device_details):
        path = '/users{}/registerdevice'.format(user_id)
        response = System._post(path=path, data=register_device_details)
        return response
