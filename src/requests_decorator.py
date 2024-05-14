import requests
from unittest.mock import patch


def get(url, params=None, orig_get=requests.get, **kwargs):
    print("before calling requests.get")
    response = orig_get(url, params, **kwargs)
    print("after calling requests.get")
    return response


request_get_validator = patch("requests.get", get)


def post(url, data=None, json=None, orig_post=requests.post, **kwargs):
    print("before calling requests.get")
    response = orig_post(url, data, json, **kwargs)
    print("after calling requests.get")
    return response


request_post_validator = patch("requests.post", post)


if __name__ == "__main__":

    @request_get_validator
    @request_post_validator
    def hello():
        r = requests.get("https://www.google.com")
        print(r.status_code)
        r = requests.get("https://www.google.com")
        print(r.status_code)
        r = requests.get("https://www.google.com")
        print(r.status_code)

    hello()
