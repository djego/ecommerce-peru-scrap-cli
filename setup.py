import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ecope',
    version='0.1.2',
    scripts=['./scripts/ecope'],
    author='Diego Machaca',
    author_email = 'diegomachaca@gmail.com',   
    url = 'https://github.com/djego/ecommerce-peru-scrap-cli',
    keywords = ['scraping', 'peru', 'ecommerce','csv','json'],
    description='Ecommerce Perú Scrap CLI is a project open source that extract products data by category and export to csv, json and other structure format files',
    packages=['application'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'setuptools',
        'beautifulsoup4 == 4.9.1',
        'html5lib == 1.1',
        'lxml == 4.5.2',
        'six == 1.15.0',
        'soupsieve == 2.0.1',
        'webencodings == 0.5.1',
        'requests == 2.24.0'
    ],
    python_requires='>=3.7'
)