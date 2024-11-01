from setuptools import setup, find_packages

setup(
    name='Bluto',
    version='2.4.18',
    maintainer=='ProjectResurrect',
    maintainer_email=='contact@boukhrisssaber.tn',
    url='https://github.com/ProjectResurrect/Bluto',
    packages=['Bluto'],
    include_package_data=True,
    license='LICENSE.txt',
    description='''
    DNS Recon | Brute Forcer | DNS Zone Transfer | DNS Wild Card Checks
    DNS Wild Card Brute Forcer | Email Enumeration | Staff Enumeration
    Compromised Account Checking''',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    scripts=['Bluto/bluto'],
    install_requires=[
    	"docopt",
        "dnspython",
        "termcolor",
        "BeautifulSoup4",
        "requests[security]",
        "pythonwhois",
        "lxml",
        "oletools",
        "pdfminer.six"
    ],
)

