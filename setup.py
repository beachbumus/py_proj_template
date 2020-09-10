from setuptools import setup, find_packages
with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name="hr",
    version="0.1",
    description='User admin functions',
    long_description=readme,
    author='Henry',
    author_email='hyip_98@linuxacadmey.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
