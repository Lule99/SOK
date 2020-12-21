from setuptools import setup, find_packages
setup(
    name="ordinary-view-plugin",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['startup'],
    entry_points = {
        'display.data':
            ['ordinary_view=startup.display_data:OrdinaryView'],
    },
    zip_safe=True
)