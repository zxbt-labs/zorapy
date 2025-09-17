# Zora Unofficial API Client

This repository is a basic Python client for the Zora API.

## Official zora docs

(Link)[https://docs.zora.co/]

## Installation

```
pip install git+https://github.com/zxbt-labs/zorapy@main
```

## Examples

```python
import os
from zorapy import ZoraPy

zora = ZoraPy(
    api_key=os.environ['ZORA_API_KEY'],
)
creator_profile = zora.call(
    endpoint='profile', 
    params={'identifier': 'zxbt'}
)

```
