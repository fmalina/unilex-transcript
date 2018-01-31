from setuptools import setup

setup(
    name="transcript",
    version="0.9.0",
    description="PDF to semantic HTML conversion.",
    author="František Malina",
    author_email='fmalina@gmail.com',
    url="https://github.com/fmalina/transcript/",
    install_requires=['lxml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    py_modules=['transcript'],
)
