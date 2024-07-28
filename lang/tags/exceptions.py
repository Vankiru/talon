from talon import Module

mod = Module()
mod.tag("code_exceptions", desc="Exception commands")
mod.list("exception_name", desc="Exceptions list")

@mod.action_class
class Actions:
    def code_exception_raise(name: str):
        """raise/throw"""

