from setuptools import setup, find_packages
setup(
    name="MathFunctions",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    scripts=['bin/calculate'],
    install_requires=['docutils>=0.3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7.x',
        'Topic :: Math Functions :: Calculas',
      ],
    author="sohaib omar",
    author_email="sohaib.omar@emumba.com",
    description="This is an package containing math functions.",
    test_suite='nose.collector',
    tests_require=['nose'],
    

)
