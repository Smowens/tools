from setuptools import setup

setup(
    name='tools',
    version='1.0',
    description="Sam's Tool Module",
    author='Sam Owens',
    author_email='sowens28@tjs.org',
    packages=['tools'],
    package_dir={'tools': 'Lib/Python Files'},
    install_requires=['setuptools', 'wheel']
)
