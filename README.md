# fatcat
![https://discord.gg/74VkcwV](https://discord.com/api/guilds/712539689638428713/embed.png) ![https://pypi.python.org/pypi/fatcat]( https://img.shields.io/pypi/v/fatcat.svg) ![https://pypi.python.org/pypi/discord.py](https://img.shields.io/pypi/pyversions/fatcat.svg)

A package written in Python to manage your servers, pterodactyl servers, and more for FatCat Hosting.

## Features
- Created using requests via api
- Customizable
- Optimized for speed

## Installing
**Python 3.6 or higher is required**

To install the library, you can just run the following command:
```sh
# Linux/macOS
python3 -m pip install -U fatcat

# Windows
py -3 -m pip install -U fatcat
```

## Examples

### Get Server Memory Usage
```py
# Getting the package
from fatcat import Server

# Creating a server class with our base URL and declaring some variables, plain & text are optional
server = Server(url="http://server_ip/", plain=False, text=True)

# Printing total server memory
print(server.total_memory())
```

### Get Active Server Memory Usage
```py
# Getting the package
from fatcat import Server

# Creating a server class with our base URL
server = Server(url="http://server_ip/")

# Printing active server memory
print(server.active_memory())
```

## Links
- [Documentation](https://fatcat.readthedocs.io/en/latest/)
- [Official Discord Server](https://discord.gg/74VkcwV)
- [PyPi](https://pypi.org/project/fatcat/)

## Contact & Support
- You can contact me on Discord at `INfoUpgraders#0001`
- [Official Support Server](https://discord.gg/Uebz9GX)
