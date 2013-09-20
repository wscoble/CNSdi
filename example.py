#!/usr/bin/env python

"""
"**CNSdi**" is a simple Python dependency injection library, build for simplicity of use.  Services can be identified through *id* and *namespace*.

[![Build Status](https://travis-ci.org/wscoble/CNSdi.png?branch=master)](https://travis-ci.org/wscoble/CNSdi)
"""

# === Decorator imports ===
from di.decorator import service, inject

# === Service examples ===

@service('a.service')
def a_service():
    return "I am a service"
    """
    Create a service with an id of *a.service* that, when retrieved, will return the *a_service* function, unmolested.
    """
    
@service('another.service', to_namespace='not.the.default.namespace')
class AnotherService(object):
    pass
    """
    Create a service that will return an instantiated object.  This time, the *namespace* is explicitly set for the service.
    """
    
# === Inject examples ===

@inject(['a.service'])
def func(svc):
    return svc()
    """
    Since *a.service* stores a function, you can call it like any other function.  The raw function stored as *a.service* is injected into this function.
    """
func() == "I am a service"

class InjectedObject(object):
    @inject(['a.service'])
    def __init__(self, svc):
        self.msg = svc()
        
    def get_message():
        return self.msg
    """
    You can inject into an class too, just do it in the constructor or any other function in the class.
    """
InjectedObject().get_message() == "I am a service"

@service('a.object.service')
class InjectedServiceObject(object):
    @inject(['a.service'])
    def __init__(self, svc):
        self.msg = svc()
    def get_message():
        return self.msg
    """
    Services can have injected functions as well.  It just works.
    """
    
# === Use helpers! ===

from di.helpers import add_service, get_service

"""
Helpers help make things a little easier for procedural code.  Here you can grab a service and start using it immediately.  No additional wiring needed.
"""
get_service('a.object.service').get_message() == "I am a service"

"""
So let's say you have a file that imports and collects all your services.
"""
from markdown import markdown
add_service('markdown', markdown)

"""
In another file, you can call up that service and use it immediately.
"""
'<h1>Hello World!</h1>' == get_service('markdown')('#Hello World!')

"""
Then you decide you want to use a different markdown renderer.
"""
from my.markdown.renderer import render
add_service('markdown', render)

"""
You call the same code in the other file, and it should work the same!
"""
'<h1>Hello World!</h1>' == get_service('markdown')('#Hello World!')