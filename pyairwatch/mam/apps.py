from .mam import MAM


class Apps(MAM):
    """
    A class to manage REST API v1 Apps
    """

    def __init__(self, client):
        MAM.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the application or book determined by the given filters.py

        /api/mam/apps/search?{params}

        PARAMS:
            type={type}
            applicationtype={applicationtype}
            applicationname={applicationname}
            productComponentAppsOnly={productComponentAppsOnly}
            category={category}
            bundleid={bundleid}
            locationgroupid={locationgroupid}
            model={model}
            status={status}
            platform={platform}
            winapptype={winapptype}
            includeAppsFromChildOgs={includeAppsFromChildOgs}
            IncludeAppsFromParentOgs={IncludeAppsFromParentOgs}
            AppCommandTarget={AppCommandTarget}
            distinctApplicationsPerOg={distinctApplicationsPerOg}
            excludeAssignedOrInstalledDeviceCount={excludeAssignedOrInstalledDeviceCount}
            page={page}
            pagesize={pagesize}
            orderby={orderby}
        """
        response = MAM._get(self, path='/apps/search', params=kwargs)
        return response

    def get_id(self, **kwargs):
        response = MAM._get(self, path='/apps/search', params=kwargs)
        return response['Application'][0]['SupportedModels']['Model'][0]['ApplicationId']

    def search_details(self, appId):
        """
        Returns details of an App searched by the ApplicationID
        """

        response = MAM._get(self, path=f'/apps/internal/{appId}')
        return response

    def check_app_installed(self, appId):
        """
        Returns a list of DeviceId's where an app determined by the given appId is installed
        """

        response = MAM._get(
            self, path=f'/apps/internal/{appId}/devices?status=installed')
        return response['DeviceId']
