import json
from eodhd import APIClient
class EODHDAPIsDataFetcher:
    def __init__(self, api_token):
        self._api_token = api_token

    def get_Exchange(self):
        try:
            api= APIClient(self._api_token)
            df=api.get_Exchange()
            return json.loads(df.to_json(orient="records"))
        except Exception as e:
            print(f"error fetching data: {e}")
            return None
    def fetch_exchange_markets(self,code: str= ""):
        try:
            api=APIClient(self._api_token)
            df=api.get_exchanges(code)
            return json.loads(df.to_json(orient="records"))
        except Exception as e:
            print(f"Error fetching data {e}")
            return None