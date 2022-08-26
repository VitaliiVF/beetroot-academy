from os import unlink

import pytest
import json

@pytest.fixture
def tmp_phonebook(tmp_path):
    
    filename = tmp_path/"data_phonebook.json"
    
    with open(filename, "w") as f:
        json.dump([{
    "first_name": "Vitalii",
    "last_name": "Fedun",
    "full_name": "Vitalii Fedun",
    "phone_number": "0988888888",
    "email": "defe@vreb.vv",
    "city": "Odesa",
    "notes": "nothing",
    "id": "b6030174-730f-4af4-b510-d668a4dc69d1"
  }], f)
    
    yield filename
    
    unlink(filename)