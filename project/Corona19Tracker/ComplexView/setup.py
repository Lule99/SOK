from setuptools import setup, find_packages
setup(
    name="complex-view-plugin",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['startup'],
    entry_points={
        'display.data':
            ['complex_view=startup.display_data:ComplexView'],
    },
    zip_safe=True
)