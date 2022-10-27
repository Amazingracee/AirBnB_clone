# 0x00. AirBnB clone - The console

> The goal of the entire project is to deploy on our server a simple copy of the AirBnB website.

### First step: Write a command interpreter to manage our AirBnB objects.

This is the first step towards building our first full web application: the AirBnB clone.
Each task is linked and will help us to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

A command line interpreter is any program that allows the entering of commands and then executes those commands to the operating system. It's literally an interpreter of commands. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my\_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my\_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my\_module").my\_function.__doc__)' and python3 -c 'print(__import__("my\_module").MyClass.my\_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test\_models/test\_base\_model.py
- e.g., For models/user.py, unit tests must be in: tests/test\_models/test\_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test\_models/test\_base\_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my\_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my\_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my\_module").my\_function.__doc__)' and python3 -c 'print(__import__("my\_module").MyClass.my\_function.__doc__)'
