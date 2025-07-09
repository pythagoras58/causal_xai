from setuptools import setup, find_packages

setup(
    name='causal_xai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'scipy',
        'matplotlib',
    ],
    author='Danso Solomon Danquah',
    author_email='solomondanso58@gmail.com',
    description='Causal Explainability for AI Models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pythagoras58/causal_xai', # Placeholder
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)