from  setuptools import setuptools,find_packages


with open('README.md') as f:
    README = f.read()
    
setuptools.setup(
    author="Harsha Veeturi",
    author_email="harshavardhanveeturi@gmail.com",
    name='speech_text',
    description='This package translates speech to text',
    version='v1.0.0',
    long_description=README,
    url='https://github.com/harshaveeturi/aganitha-cognitive',
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=['spacy','word2number'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
