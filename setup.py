from setuptools import setup, find_packages

# Load Requirements
with open('requirements.txt') as f:
    requirements = f.readlines()

# For the cases you want a different package to be installed on local and prod environments
# import subprocess
# LOCAL_ARG = '--local'
# if LOCAL_ARG in sys.argv:
#     index = sys.argv.index(LOCAL_ARG)  # Index of the local argument
#     sys.argv.pop(index)  # Removes the local argument in order to prevent the setup() error
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'A package that works locally'])
# else:
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'A package that works on production'])

# Load README
with open('README.md') as readme_file:
    readme = readme_file.read()

setup_requirements = []
test_requirements = []

COMMANDS = [
    'greet = starter.cli:greet',
    'starter_main = starter.main:main'
]

data_files = ['starter/configuration/yml_schema.json']

setup(
    author="drkostas",
    author_email="georgiou.kostas94@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    data_files=[('', data_files)],
    description="A starter template for Python packages.",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='starter',
    name='starter',
    # package_dir={'': '.'},
    packages=find_packages(include=['starter', 'starter.*']),
    # py_modules=['main'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/drkostas/starter',
    version='0.1.0',
    zip_safe=False,
)
