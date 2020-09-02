from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
]

setup(name='fatcat',
      author='INfoUpgraders',
      url='https://github.com/INfoUpgraders/fatcat',
      project_urls={
        "Documentation": "https://fatcat.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/INfoUpgraders/fatcat/issues",
      },
      version='0.0.7',
      packages=find_packages(),
      license='MIT',
      description='A python package for FatCat Hosting',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=['requests>=2.20.0'],
      extras_require={'docs': ['sphinx==1.8.5', 'sphinxcontrib_trio==1.1.1', 'sphinxcontrib-websupport']},
      python_requires='>=3.6',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
