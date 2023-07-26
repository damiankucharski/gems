from dask.distributed import Client, LocalCluster


class LocalRunner:
    def __init__(self):
        self.cluster = LocalCluster()
        self.client = Client(self.cluster)  

    def map_function(self, func, iterables):
        futures = self.client.map(func, iterables)
        return futures
    
    def gather_futures(self, futures):
        return self.client.gather(futures)

    def get_dashboard_adress(self):
        return self.client.dashboard_link

    def get_failed_futures(self, futures):
        return [future for future in futures if future.status == "error"]

    def get_successful_futures(self, futures):
        return [future for future in futures if future.status == "finished"]
