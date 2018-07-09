import requests
from retrying import retry


class RetryRequest(object):
    def __init__(self):
        self.url = 'http://bai'
        self.index = 0

    @retry(stop_max_attempt_number=5)
    def _request_data(self):
        self.index +=1
        print(self.index)
        response = requests.get(self.url)

        # 断言status一定为200
        assert response.status_code == 200
        return response


    def run(self):
        try:
            data = self._request_data()
            print(data)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    RetryRequest().run()