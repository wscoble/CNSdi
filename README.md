# CNS DI

[![Build Status](https://travis-ci.org/wscoble/CNSdi.png?branch=master)](https://travis-ci.org/wscoble/CNSdi)

CNS Dependency Injection is a very simple way to store and inject services into your software.

It looks like this for Flask (dumb example, but you should get the point)::

    from di.helpers import get_service, add_service
    from di.decorator import service, inject
    from flask import Flask

    app = Flask(__name__)
    add_service('router', app.route)

    @service('adder')
    def adder(*args):
      sum = 0
      for arg in args:
        sum += arg
      return sum

    router = get_service('router')

    @router('/adds')
    def adds():
      sum = get_service('adder')([1,2,3])
      return "hello " + repr(sum)

    get_service('app').run()

If you are going to @inject into a class, do it on the __init__ function.  @service can be used with classes or functions.