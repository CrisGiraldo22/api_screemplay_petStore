import requests

class CallApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()


    def get(self, endponit, **kwargs):
        return self.session.get(f"{self.base_url}{endponit}", **kwargs)    