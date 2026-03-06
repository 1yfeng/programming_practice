import pytest
from src.demo import module_function, DemoClass

def test_module_function():
    module_function()
    demo = DemoClass("TestDemoClass")
    demo.demo_function()
    