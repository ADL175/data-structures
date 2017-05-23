from setuptools import setup

setup(
    name="Linked List and Stack",
    description="Linked List and Stack in Python",
    version="0.1",
    author="David Lim, Ronel Rustia, Erik Enderlein",
    author_email="armydavidlim@gmail.com",
    license="MIT",
    py_modules=['linked_list', 'stack'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test':['pytest','pytest-watch', 'pytest-cov', 'ipython']},
    entry_points={
        'console_scripts':[
            "linked_list = linked_list:main",
            "stack = stack:main"
            ]
    }
    )
