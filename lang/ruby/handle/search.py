from talon import Module, Context, actions

mod = Module()
mod.list("nameless_token_regex", desc="Regex for nameless tokens")
mod.list("number_token_regex", desc="Regex for number tokens")
mod.list("text_token_regex", desc="Regex for text tokens")
mod.list("snake_name_token_regex", desc="Regex for snake name tokens")
mod.list("class_name_token_regex", desc="Regex for class name tokens")
mod.list("const_name_token_regex", desc="Regex for const name tokens")
mod.list("file_name_token_regex", desc="Regex for file name tokens")

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

# for <item> in <list>
# for item in list do
# number <number> point <number>
# range <from> to <to> (from..to)
# range <from> until <to> (from...to)
# object range <from> to <to> Range.new(from, to)
# object range <from> until <to> Range.new(from, to, true)
# rescue <name> as <name> rescue Name => name
# set <name> to: "name =",

ctx.lists["user.nameless_token_regex"] = {
    # arguments
    "arts": "(.*)",
    "barbs": " |.*|",
    "comma": ",[ |\\n]",
    "forward art": "(\zs\.\.\.\ze)",
    # blocks
    "block": "\([while|until] .*\)\@<! do",
    "line block": "\w\+\zs {.*}",
    # classes
    "self class": "class << self",
    "class init": "def initialize",
    "private": "private",
    "protected": "protected",
    "public": "public",
    # comments
    "frozen string": "# frozen_string_literal: true",
    "magic encode": "# encoding: ",
    "magic warn": "# warn_indent: ",
    "magic share": "# shareable_constant_value: ",
    "magic share none": "# shareable_constant_value: none",
    "magic share lit": "# shareable_constant_value: literal",
    "magic share every": "# shareable_constant_value: experimental_everything",
    "magic share copy": "# shareable_constant_value: experimental_copy",
    # controls
    "if": "\(els\)\@<!if",
    "else": "else",
    "else if": "elsif",
    "unless": "unless",
    "leaf": " if",
    "unleaf": " unless",
    "triplet": "? .* : .*",
    "case": "case",
    "when": "when",
    "then": "then",
    "while": "while",
    "until": "until",
    "end while": "end while",
    "line while": " while",
    "line until": " until",
    "break": "break",
    "break if": "break if",
    "next": "next",
    "next if": "next if",
    # data types
    "true": "true",
    "false": "false",
    "none": "nil",
    "nun": "nil",
    "list": "\(\w\+\)\@<!\[",
    "object list": "Array\.new",
    "string list": "%w\[",
    "sim list": "%i\[",
    "hash": "\([\w\+ |#]\)\@<!{",
    "object hash": "Hash\.new",
    "set": "Set\.new",
    "lambda": "-> {",
    # exceptions
    "begin": "\(=\)\@<!begin",
    "ensure": "ensure",
    "retry": "retry",
    # methods
    "return": "return",
    "parent": "super",
    "yeild": "yield",
    "yeild self": "yeild self",
    # operators
    "set to": " = ",
    "plus": " + ",
    "minus": " - ",
    "multi": " \* ",
    "divide": " \/ ",
    "modulus": " % ",
    "power": "\*\*",
    "plus equal": " += ",
    "minus equal": " -= ",
    "multi equal": " \*= ",
    "divide equal": " \/= ",
    "mod equal": " %= ",
    "power equal": " \*\*= ",
    "equal": " == ",
    "not equal": " != ",
    "great": " > ",
    "less": " < ",
    "great equal": " >= ",
    "less equal": " <= ",
    "compare": " <=> ",
    "test equal": " === ",
    "add | also": " && ",
    "or | either": " || ",
    "not": " !",
    "text add | also": " and ",
    "text or | either": " or ",
    "text not": " not ",
    "index": "\w\+\zs\[.*\]",
    "inside": " in ",
    "match": " => ",
    "bit and": " & ",
    "bit or": " | ",
    "bit ex": " ^ ",
    "bit not": " ~ ",
    "bit left": " << ",
    "bit right": " >> ",
    # statements
    "art read": "attr_reader ",
    "art write": "attr_writer ",
    "art access": "attr_accessor ",
    # library
    "print": "puts",
}

ctx.lists["user.number_token_regex"] = {
    # data types
    "number": "{identifier}",
    "range": "({identifier}\d*..)",
    "range to": "(\.\.{identifier}\d*)",
    "range by": "(\.\.{identifier}\d*)",
    "range until": "(\.\.\.{identifier}\d*)",
}

ctx.lists["user.text_token_regex"] = {
    # comments
    "remark": "^# {identifier}.*",
    "line remark": " # {identifier}.*",
    "multi remark": "=begin\n\zs{identifier}.*",
    # data types
    "string": '"{identifier}.*"',
    "quote string": "'{identifier}.*'",
    "multi string": '"\n{identifier}.*"',
    "doc string": "<<~DOC\n{identifier}.*",
    "rig": "\/{identifier}.*\/"
}

ctx.lists["user.snake_name_token_regex"] = {
    # arguments
    "default": "\({identifier}\)\@<!: .*, ",
    "list art": "\(*\)\@<!\*{identifier}",
    "hash art": "\*\*{identifier}",
    "key art": "{identifier}:",
    "block art": "&{identifier}",
    # data types
    "interpol": "#{{{identifier}}}",
    "sim": ":{identifier}",
    "key": "{identifier}: ",
    "string key": '"{identifier}": ',
    "object key": "{identifier} => ",
    # exceptions
    "rescue as": "rescue => {identifier}",
    # methods
    "met": "def {identifier}",
    "short met": "def {identifier} = ",
    "met bank": "def {identifier}!",
    "mukbang": "def {identifier}!",
    "met plight": "def {identifier}?",
    "call": ".{identifier}",
    "call bang": ".{identifier}!",
    "call plight": ".{identifier}?",
    "safe call": "&.{identifier}",
    # names
    "name": "{identifier}",
    "bang": "{identifier}!",
    "plight": "{identifier}?",
    "instance": "@{identifier}",
    "type instance": "@@{identifier}",
    "self": "self.{identifier}",
    "global": "${identifier}",
    # statements
    "unbind": "undef {identifier}",
    "defined": "defined?({identifier})"
}

ctx.lists["user.class_name_token_regex"] = {
    # classes
    "class": "class {identifier}",
    "superclass": "class \(::\)\?\w\+\(::\w\+\)*\zs < {{identifier}} ",
    "new": "{identifier}\.new\((.*)\)\?",
    # exceptions
    "raise": "raise {identifier}",
    "rescue": "rescue {identifier}",
    # modules
    "module": "module {identifier}",
    "refine": "refine {identifier}",
    "include": "include {identifier}",
    "extend": "extend {identifier}",
    "using": "using {identifier}",
    # names
    "type": "{identifier}",
    "pack": "::{identifier}"
}

ctx.lists["user.const_name_token_regex"] = {
    # names
    "const": "{identifier}",
}

ctx.lists["user.file_name_token_regex"] = {
    # statements
    "require": 'require "{identifier}.*"',
}

@mod.action_class
class Actions:
    def code_go_to_token(token: str, identifier: str = ""):
        """Go to the next token"""

    def code_back_to_token(token: str, identifier: str = ""):
        """Go to the next token"""

    def code_search_token(token: str, identifier: str = "", direction: str = "/"):
        """Search for a token"""

@ctx.action_class("user")
class CodeActions:
    def code_go_to_token(token: str, identifier: str = ""):
        actions.user.code_search_token(token, identifier)
        actions.user.vim_command_mode("noh")

    def code_back_to_token(token: str, identifier: str = ""):
        actions.user.code_search_token(token, identifier, "?")
        actions.user.vim_command_mode("noh")

    def code_search_token(token: str, identifier: str = "", direction: str = "/"):
        search = f"{direction}{token.format(identifier = identifier)}"
        actions.user.vim_normal_mode(search)
        actions.key("enter")
