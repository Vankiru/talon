from talon import Context, Module, actions

mod = Module()
ctx = Context()

CODE_ANNOTATION_TYPES = {
        "bool": "bool",
        "number": "int",
        "integer": "int",
        "float": "float",
        "complex": "complex",
        "string": "str",
        "any": "Any"
        }

@mod.capture(rule="bool|number|integer|float|complex|string|any")
def code_annotation_type(m) -> str:
    return CODE_ANNOTATION_TYPES[str(m)]
