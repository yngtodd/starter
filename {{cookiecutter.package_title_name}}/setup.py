from setuptools import setup, find_packages, Command
import os


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


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
    'cli = {{cookiecutter.package_name}}.cli:app',
    '{{cookiecutter.package_name}}_main = {{cookiecutter.package_name}}.main:main'
]

data_files = ['{{cookiecutter.package_name}}/configuration/yml_schema.json']

setup(
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
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
    cmdclass={
        'clean': CleanCommand,
    },
    data_files=[('', data_files)],
    description="{{cookiecutter.package_description}}",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='{{cookiecutter.package_name}}',
    name='{{cookiecutter.package_name}}',
    # package_dir={'': '.'},
    packages=find_packages(include=['{{cookiecutter.package_name}}',
                                    '{{cookiecutter.package_name}}.*']),
    # py_modules=['main'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='{{cookiecutter.github_url}}',
    version='{{cookiecutter.package_version}}',
    zip_safe=False,
)
