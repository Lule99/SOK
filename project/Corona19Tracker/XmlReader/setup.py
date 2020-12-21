from setuptools import setup, find_packages
setup(
    name="xml-reader-plugin",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['startup'],
    entry_points={
        'data.reading':
            ['reading_file=startup.read_file:XmlReader'],
    },
    data_files=[('data', ['../data/xml/dataset1.xml'])],
    zip_safe=False
)