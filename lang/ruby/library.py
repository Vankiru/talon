from talon import Module, Context, actions

mod = Module()
mod.list("std_method", desc="Standard library methods")

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

ctx.lists["user.std_method"] = {
        "to integer": "to_i",
        "to float": "to_f",
        "to rational": "to_r",
        "to decimal": "to_d",
        "to string": "to_s",
        "to list": "to_a",
        "to hash": "to_h"
}

ctx.lists["user.std_block_method"] = {
}

@ctx.action_class("user")
class CodeActions:
    pass
