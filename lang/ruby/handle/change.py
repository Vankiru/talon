from talon import Module, Context, actions

mod = Module()

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"
# "rescue as": "rescue => {id}",
# for <item> in <list>
# for item in list do
# number <number> point <number>
# range <from> to <to> (from..to)
# range <from> until <to> (from...to)
# object range <from> to <to> Range.new(from, to)
# object range <from> until <to> Range.new(from, to, true)
# rescue <name> as <name> rescue Name => name
# set <name> to: "name =",

ctx.lists["user.nameless_token"] = {
    # arguments
    "comma": "comma",
    "forward art": "forward art",
    # comments
    "frozen string": "frozen string",
    "magic share none": "magic share none",
    "magic share lit": "magic share lit",
    "magic share every": "magic share every",
    "magic share copy": "magic share copy",
    # data types
    "true": "true",
    "false": "false",
    "none": "none",
    "nun": "nun",
    "object list": "object list",
    "set": "set",
    "object hash": "object hash",
    # exceptions
    "ensure": "ensure",
    "retry": "retry",
    # operators
    "set to": "set to",
    "plus": "plus",
    "minus": "minus",
    "multi": "multi",
    "divide": "divide",
    "modulus": "modulus",
    "power": "power",
    "plus equal": "plus equal",
    "minus equal": "minus equal",
    "multi equal": "multi equal",
    "divide equal": "divide equal",
    "mod equal": "mod equal",
    "power equal": "power equal",
    "equal": "equal",
    "not equal": "not equal",
    "great": "great",
    "less": "less",
    "great equal": "great equal",
    "less equal": "less equal",
    "compare": "compare",
    "test equal": "test equal",
    "add | also": "add | also",
    "or | either": "or | either",
    "not": "not",
    "text add | also": "text add | also",
    "text or | either": "text or | either",
    "text not": "text not",
    "index": "index",
    "inside": "inside",
    "match": "match",
    "bit and": "bit and",
    "bit or": "bit or",
    "bit ex": "bit ex",
    "bit not": "bit not",
    "bit left": "bit left",
    "bit right": "bit right"
}

ctx.lists["user.name_token"] = {
    # arguments
    "default": "\({identifier}\)\@<!: .*, ",
    "list art": "\(*\)\@<!\*{identifier}",
    "hash art": "\*\*{identifier}",
    "key art": "{identifier}:",
    "block art": "&{identifier}",
    # blocks
    "block": "\([while|until] .*\)\@<! do",
    "line block": "\w\+\zs {.*}",
    # comments
    "magic encode": "# encoding: ",
    "magic warn": "# warn_indent: ",
    "magic share": "# shareable_constant_value: ",
    # classes
    "class": "class {identifier}",
    "rescue": "rescue {identifier}",
    "module": "module {identifier}",
    "refine": "refine {identifier}",
    "superclass": "class \(::\)\?\w\+\(::\w\+\)*\zs < {{identifier}} ",
    "new": "{identifier}\.new\((.*)\)\?",
    # controls
    "if": "\(els\)\@<!if",
    "else if": "elsif",
    "unless": "unless",
    "leaf": " if",
    "unleaf": " unless",
    "triplet": "? .* : .*",
    "case": "case",
    "when": "when",
    "while": "while",
    "until": "until",
    "end while": "end while",
    "line while": " while",
    "line until": " until",
    "break": "break",
    "next": "next",
    "break if": "break if",
    "next if": "next if",
    # data types
    "number": "{identifier}",
    "sim": ":{identifier}",
    "key": "{identifier}: ",
    "string key": '"{identifier}": ',
    "object key": "{identifier} => ",
    "range": "({identifier}\d*..)",
    "range to": "(\.\.{identifier}\d*)",
    "range by": "(\.\.{identifier}\d*)",
    "range until": "(\.\.\.{identifier}\d*)",
    # exceptions
    "raise": "raise {identifier}",
    # methods
    "met": "def {identifier}",
    "met bank": "def {identifier}!",
    "mukbang": "def {identifier}!",
    "met plight": "def {identifier}?",
    "short met": "def {identifier} = ",
    "call": ".{identifier}",
    "call bang": ".{identifier}!",
    "call plight": ".{identifier}?",
    "safe call": "&.{identifier}",
    # modules
    "include": "include {identifier}",
    "extend": "extend {identifier}",
    "using": "using {identifier}",
    # names
    "name": "{identifier}",
    "bang": "{identifier}!",
    "plight": "{identifier}?",
    "instance": "@{identifier}",
    "type instance": "@@{identifier}",
    "self": "self.{identifier}",
    "global": "${identifier}",
    "const": "{identifier}",
    "type": "{identifier}",
    "pack": "::{identifier}"
    # statements
    "unbind": "undef {identifier}",
    "defined": "defined?({identifier})"
    "require": 'require "{identifier}.*"'
}

ctx.lists["user.line_token"] = {
    # arguments
    "arts": "(.*)",
    "barbs": " |.*|",
    # blocks
    "line block": "\w\+\zs {.*}",
    # classes
    "private": "private",
    "protected": "protected",
    "public": "public",
    # comments
    "remark": "^# {identifier}.*",
    "line remark": " # {identifier}.*",
    # controls
    "leaf": " if",
    "unleaf": " unless",
    "triplet": "? .* : .*",
    "then": "then",
    "line while": " while",
    "line until": " until",
    # data types
    "list": "\(\w\+\)\@<!\[",
    "string list": "%w\[",
    "sim list": "%i\[",
    "hash": "\([\w\+ |#]\)\@<!{",
    "string": '"{identifier}.*"',
    "quote string": "'{identifier}.*'",
    "interpol": "#{{{identifier}}}",
    "rig": "\/{identifier}.*\/"
    "lambda": "-> {",
    # methods
    "short met": "def {identifier} = ",
    "return": "return",
    "parent": "super",
    "yeild": "yield",
    "yeild self": "yeild self",
    # statements
    "art read": "attr_reader ",
    "art write": "attr_writer ",
    "art access": "attr_accessor ",
    "print": "puts",
}

ctx.lists["user.block_token"] = {
    # blocks
    "block": "block",
    # classes
    "class": "class",
    "self class": "self class",
    "class init": "class init",
    # comments
    "multi remark": "multi remark",
    # controls
    "if": "if",
    "else": "else",
    "else if": "else if",
    "unless": "unless",
    "case": "case",
    "when": "when",
    "while": "while",
    "until": "until",
    "end while": "end while",
    # exceptions
    "begin": "begin",
    "rescue": "rescue",
    # data types
    "multi string": "multi string",
    "doc string": "doc string",
    # methods
    "met": "met",
    "met bank": "met bank",
    "mukbang": "mukbang",
    "met plight": "met plight",
    # modules
    "module": "module",
    "refine": "refine"
}
