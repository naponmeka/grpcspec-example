from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='pygrpcspec',
    version='0.0.1',
    description='grpc spec',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=['pygrpcspec','pygrpcspec.proto'],
    # packages=find_packages(include=['pybrijgrpc', 'pyybrijgrpc/proto']),
    author='Napon Mekavuthikul',
    author_email='napon.meka@gmail.com.com',
    keywords=['grpc'],
    url='https://github.com/naponmeka/grpcspec-example',
    download_url=''
)

install_requires = [
    'grpcio>=1.21.0',
    'grpcio-tools>=1.21.0',
    'protobuf>=3.8.0'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)