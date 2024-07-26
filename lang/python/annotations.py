from talon import Module, Context

mod = Module()
mod.list("code_python_annotation_type", desc="Python annotation types")

ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

ctx.lists["user.code_python_annotation_type"] = {
    "bool": "bool",
    "number": "int",
    "integer": "int",
    "float": "float",
    "complex": "complex",
    "string": "str",
    "any": "Any"
}
