from setuptools import setup, find_packages
setup(
    name="text-reader-plugin",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['startup'],
    entry_points={
        'data.reading':
            ['reading_file=startup.read_file:TextReader'],
    },
    data_files=[('data', ['../data/txt/dataset1.txt'])],
    zip_safe=False
)