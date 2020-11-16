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