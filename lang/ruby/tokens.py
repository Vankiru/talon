from talon import Module, Context, actions

mod = Module()
mod.list("token_regex", desc="")

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

class_name_regex = "\(::\)\?\w\+\(::\w\+\)*"

ctx.lists["user.token_arguments_regex"] = {
    "arts": "(.*)",
    "barbs": " |.*|",
    "comma": ",[ |\n]",
    "default": "\w\+:", # name
    "list art": "^*\*\w\+", # name
    "hash art": "\*\*\w\+" # <name>
    "key art": "\w\+:", # name
    "block art": "&\w\+", # <name>
    "forward art": "(\.\.\.)"
}

ctx.lists["user.token_blocks_regex"] = {
    "block": "\([while|until] .*\)\@<! do",
    "line block": "\w\+\zs {.*}"
}

ctx.lists["user.token_classes_regex"] = {
    "class": "class ", # <name>
    "self class": "class << self",
    "superclass": f"class {class_name_regex}\zs < ", #  <name>
    "class init": "def initialize",
    "private": "private",
    "protected": "protected",
    "public": "public",
    "new": f"{class_name_regex}\.new" # name
}


ctx.lists["user.token_comments_regex"] = {
    "remark": "^#", # <text>
    "line remark": " # ", # text
    "multi remark": "=begin", # <text>
    "frozen string": "# frozen_string_literal",
    "magic encode": "# encoding",
    "magic warn": "# warn_indent",
    "magic share none": "# shareable_constant_value: none",
    "magic share lit": "# shareable_constant_value: literal",
    "magic share every": "# shareable_constant_value: experimental_everything",
    "magic share copy": "# shareable_constant_value: experimental_copy"
}

# for <item> in <list>
# for item in list do
ctx.lists["user.token_controls_regex"] = {
    "if": " \{2,}\zsif",
    "else": "else",
    "else if": "elsif",
    "unless": " \{2,}\zsunless",
    "leaf": " if ",
    "unleaf": " unless ",
    "triplet": "? .* : .*",
    "case": "case",
    "when": "when",
    "then": "then",
    "while": " \{2,}\zswhile",
    "until": " \{2,}\zsuntil",
    "end while": "end while",
    "line while": " while ",
    "line until": " until ",
    "break": "break",
    "break if": "break if",
    "next": "next",
    "next if": "next if"
}

# number <number> point <number>
# range <from> to <to> (from..to)
# range <from> until <to> (from...to)
# object range <from> to <to> Range.new(from, to)
# object range <from> until <to> Range.new(from, to, true)
ctx.lists["user.token_data_types_regex"] = {
    "true": "true",
    "false": "false",
    "none": "nil",
    "nun": "nil",
    "number": "\d\+", # <number>
    "string": '".*"', # text
    "quote string": "'.*'", # <text>
    'multi string": '"\n"', # <text>
    "interpol": "#{.*}", # <name>
    "doc string" "<<~DOC", # <text>
    "sim": ":\w\+", # <name>
    "list": "\[.*\]",
    "multi list": "\[\n\]",
    "object list": "Array.new",
    "string list": "%w\[.*\]",
    "sim list": "%i\[.*\]",
    "hash": "{.*}",
    "multi hash": "{\n}",
    "object hash": "Hash.new",
    "key": "\w\+: ", # key
    "string key": '"\w\+": '# <key>
    "object key": "\w\+ => ", # <key> to
    "set": "Set\.new",
    "range": "(\d\+..)", # <from>
    "range to": "(..\d\+)", # <to>
    "range until": "(...\d\+)", # <to>
    "rig": "\/.*\/", # <text>
    "lambda": "-> {"
}

# rescue <name> as <name> rescue Name => name
ctx.lists["user.token_exceptions_regex"] = {
    "raise": "raise {class_name_regex}", # <name>
    "begin": "begin",
    "rescue": "rescue" # name
    "rescue as": "rescue => \w\+", # name
    "ensure": "ensure",
    "retry": "retry"
    }

ctx.lists["user.token_libraries_regex"] = {
        "print": "print" # <text>
        }


ctx.lists["user.token_methods_regex"] = {
    "met": "def {method_name}", # <name>
    "short met": "def {method_name} = ",
    "met bank": "def {name}!",
    "mukbang": "def {name}!",
    "met plight": "def {name}?",
    "return": "return",
    "parent": "super",
    "yeild": "yield",
    "yeild self": "yeild self",
    "call": ".{name}",
    "call bang": ".{name}!",
    "call plight": ".{name}?",
    "safe call": "&.{name}",
    }

ctx.lists["user.token_modules_regex"] = {
    "module <module_name>": "module ModuleName",
    "refine <class_name>": "refine ClassName",
    "include <module_name>": "include ModuleName",
    "extend <module_name>": "extend ModuleName",
    "using <module_name>": "using ModuleName"
    }

ctx.lists["user.token_names_regex"] = {
    "name <name>": "name",
    "bang <name>": "name!",
    "plight <name>": "name?",
    "instance <name>": "@name",
    "type instance <name>": "@@name",
    "self <name>": "self.name",
    "const <name>": "NAME",
    "type <name>": "Name",
    "pack <name>": "::Name",
    "global <name>": "$name"
    }

ctx.lists["user.token_operators_regex"] = {
    "set to": "=",
    "set <name> to": "name =",

    "plus": "+",
    "minus": "-",
    "multi": "*",
    "divide": "/",
    "modulus": "%",
    "power": "**",

    "plus equal": "+=",
    "minus equal": "-=",
    "multi equal": "-=",
    "divide equal": "/=",
    "mod equal": "%=",
    "power equal": "**=",

    "equal": "==",
    "not equal": "!=",
    "great": ">",
    "lest": "<",
    "great equal": ">=",
    "lest equal": "<=",
    "compare": "<=>",
    "test equal": "===",

    "add | also": "&&",
    "or | either": "||",
    "not": "!",
    "text add | also": "and",
    "text or | either": "or",
    "text not": "not",

    "index": "[]",
    "inside": "in",
    "match": "=>",

    "bit and": "&",
    "bit or": "|",
    "bit ex": "^",
    "bit not": "~",
    "bit left": "<<",
    "bit right": ">>"
    }

ctx.lists["user.token_statements_regex"] = {
    "require <path>": "require "path"",
    "unbind <name>": "undef name",
    "defined <name>": "defined?(name)",
    "art read": "attr_reader",
    "art write": "attr_writter",
    "art access": "attr_accessor",
    }

@ctx.action_class("user")
class CodeActions:
    pass

