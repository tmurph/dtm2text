import setuptools as tools


def readme():
    with open('README.rst') as f:
        return f.read()


tools.setup(
    name='dtm2text',
    version='0.0.6',
    description='Dump Dolphin TAS Movie files to plain text, and construct DTM from the same.',
    url='https://github.com/tmurph/dtm2text',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    long_description=readme(),
    author='Trevor Murphy',
    author_email='trevor.m.murphy@gmail.com',
    scripts=['dtm2text.py'],
    packages=tools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dtm2text=dtm2text:dtm2text',
            'text2dtm=dtm2text:text2dtm'
        ]
    }
)
