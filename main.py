from pyairwatch.client import AirWatchAPI

a = AirWatchAPI(env='https://as801.awmdm.com',
                apikey='48RHTtFHt5NmujBLctmr4//29lhtngYEG+fkBE9ixFM=',
                username='td.fuchs.marco',
                password='yf$8@9Nv3J^N3#s6^#&84Y4s')

gid = a.groups.get_id_from_groupid(groupid='tisp_fuchsm')
print(gid)