from setuptools import setup
setup(
    name='tools',
    version='1.1',
    description="Sam's Tool Module",
    author='Sam Owens',
    author_email='sowens28@tjs.org',
    packages=['tools'],
    py_modules=['tools','setup'],
    install_requires=['setuptools', 'wheel']
)
