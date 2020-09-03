fatcat
======

|Official Discord| |Official PyPi| |Python Versions|

A package written in Python to manage your servers, pterodactyl servers,
and more for FatCat Hosting.

Features
--------

-  Created using requests via api
-  Customizable
-  Optimized for speed

Installing
----------

**Python 3.6 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U fatcat

    # Windows
    py -3 -m pip install -U fatcat

Examples
--------

Get Server Memory Usage
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

    # Getting the package
    from fatcat import Server

    # Creating a server class with our base URL and declaring some variables, plain & text are optional
    server = Server(url="http://server_ip/", plain=False, text=True)

    # Printing total server memory
    print(server.total_memory())

Get Active Server Memory Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

    # Getting the package
    from fatcat import Server

    # Creating a server class with our base URL
    server = Server(url="http://server_ip/")

    # Printing active server memory
    print(server.active_memory())

Links
-----

-  `Documentation <https://fatcat.readthedocs.io/en/latest/>`__
-  `Official Discord Server <https://discord.gg/74VkcwV>`__
-  `PyPi <https://pypi.org/project/fatcat/>`__

Contact & Support
-----------------

-  You can contact me on Discord at ``INfoUpgraders#0001``
-  `Official Support Server <https://discord.gg/Uebz9GX>`__

.. |Official Discord| image:: https://discord.com/api/guilds/712539689638428713/embed.png
   :target: https://discord.gg/74VkcwV
.. |Official PyPi| image:: https://img.shields.io/pypi/v/fatcat.svg
   :target: https://pypi.python.org/pypi/fatcat
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/fatcat.svg
   :target: https://pypi.python.org/pypi/fatcat
