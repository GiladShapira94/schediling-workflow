from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

funcs = {}

# init functions is used to configure function resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(auto_mount())



def kfpipeline():
    with dsl.ParallelFor([{'a': 1, 'b': 10}, {'a': 2, 'b': 20}]) as item:
        op1 = funcs['op1'].as_step(params={"num":item.a})
        op2 = funcs['op2'].as_step(params={"num":item.b})