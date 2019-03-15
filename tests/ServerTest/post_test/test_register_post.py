from Server.bin.server import data_202
from Server.util.utils import data_encode

input_201 = {
    "status": "ok",
    "content": {
        "name": "zzk",
        "time": "2019-.3"
    },
    "msg": {
        "code": 201,
        "docs": ""
    }}

input_202 = {
    "status": "ok",
    "content": {
        "from": "zzk",
        "to": "all",
        "time": "2019.3",
        "content": "hello world"
    },
    "msg": {
        "code": 202,
        "docs": ""
    }
}


def test_demo():
    real_output = data_202(input_202)
    data = {
        "status": "ok",
        "content": {
            "from": "zzk",
            "to": "all",
            "time": "2019.3",
            "content": "hello world"
        },
        "msg": {
            "code": 202,
            "docs": ""
        }
    }
    expect_output = data_encode(data)
    assert real_output == expect_output
