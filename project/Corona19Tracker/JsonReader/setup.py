from setuptools import setup, find_packages
setup(
    name="json-reader-plugin",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['startup'],
    entry_points = {
        'data.reading':
            ['reading_file=startup.read_file:JsonReader'],
    },
    data_files=[('data',['../data/json/dataset1.json'])],
    zip_safe=False
)