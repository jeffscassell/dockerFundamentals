"""
frontend.main
~~~~~~~~~~~~~

Here is a docstring for this module.
"""

import requests



response = requests.get("http://backend:8080", timeout=5)
print("/")
try:
    print("JSON", response.json())
except BaseException:
    print("No JSON")

print("Headers", response.headers)
print("Text", response.text)
print()

response = requests.get("http://backend:8080/string", timeout=5)
print("/string")
try:
    print("JSON", response.json())
except BaseException:
    print("No JSON")

print("Headers", response.headers)
print("Text", response.text)
print()
