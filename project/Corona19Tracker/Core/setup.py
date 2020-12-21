from setuptools import setup, find_packages
setup(
    name="corona19-tracker-core",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['startup'],
    provides=['startup.services',
              ],
    entry_points = {
        'console_scripts':
            ['main=startup.console_main:main'],
    },
    zip_safe=True
)