from .system import System


class Tags(System):
    """
    Get Tag information under the System API
    """

    def __init__(self, client):
        System.__init__(self, client)

    def get_by_group_id(self, id):
        """
        Gets the list of tags for the given organization group 
        Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).

        /api/system/groups/{id}/tags

        PARAMS:
            id={id}
        """

        response = System._get(self, path=f'/groups/{id}/tags')
        return response
