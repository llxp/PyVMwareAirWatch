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

    def get_user_by_id(self, uuid):
        """
        Returns the enrollment user for a specific uuid using the v2 endpoint.

        PARAMS:
            uuid (str): AirWatch UUID to return
        """
        _path = "/users/{}".format(uuid)
        _header = {'Accept': 'application/json;version=2'}
        return System._get(self, header=_header, path=_path)

    def update_user_by_id(self, uuid: str=None, **kwargs):
        """
        Update the enrollment user with attributes using the v2 endpoint that supports Access.

        /api/system/users/{uuid}

        PARAMS:
            password={Password1}
            firstName={Firstname}
            lastName={Lastname}
            displayName={displayName}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.com}
            phoneNumber={5551234567}
            mobileNumber={5551234567}
            messageType={Email}
            messageTemplateUuid={2aca918b-3468-4539-8750-41a7074b120d}
            deviceStagingEnabled": false,
            deviceStagingType={StagingDisabled}
            enrollmentRoleUuid={0aa0256e-89c6-450e-854c-aa97233b61b6}
            enrollmentOrganizationGroupUuid={db1d3802-6885-4035-99ab-e39239b5a0f2}
            CustomAttribute1={CustomAttribute1}
            CustomAttribute2={CustomAttribute2}
            CustomAttribute3={CustomAttribute3}
            CustomAttribute4={CustomAttribute4}
            CustomAttribute5={CustomAttribute5}
        """
        _path = "/users/{}".format(uuid)
        _header = {'Accept': 'application/json;version=2'}
        return System._put(self, path=_path, header=_header, json=kwargs)

    def delete_user_by_id(self, user_id):
        """
        Delete the enrollment user by enrollment user id

        :param user_id:
        :return: API response
        """
        path = '/users/{}/delete'.format(user_id)
        return System._delete(self, path=path)

    def create_device_registration_to_user(self, user_id, register_device_details):
        path = '/users/{}/registerdevice'.format(user_id)
        response = System._post(path=path, data=register_device_details)
        return response
