from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
title: /VIM/
"""

@mod.action_class
class Actions:
    def constant_name(names: list):
        """Generate a name for a constant"""

@ctx.action_class("user")
class PythonActions:
    def constant_name(names: list):
        """Generate a name for a constant"""

        for name in names:
            print("python" + name)

        return names

