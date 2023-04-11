# LodiProxy

A simple project for a proxy using AWS lambda functions and pickle to proxy get and post requests from AWS servers.

### For deploying on AWS:

```bash
pip3 install requirements.txt
zappa init
zappa deploy [stage] # Where stage can be [dev, staging, production]
```
Zappa setting in current 

### You python code:
```python
import pickle, requests

x = requests.post(url='your http to lambda function', json={})
#x = requests.get(url='your http to a get lambda function')

if x.status_code != 200:
    raise Exception("Sorry, some errors occurred.")

x = pickle.loads(x.content)
```