VALUE_REGEX = "\([[:alnum:]_\"',\. @$\[\]{}()]\+\|:\w\+\)"

RUBY_DATA_TYPES_TOKENS = {
    "true": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "true"
    },
    "false": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "false"
    },
    "none": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "nil"
    },
    "nun": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "nil"
    },
    "number": {
        "type": "inline",
        "id_type": "string_number",
        "search_regex": "{id}\d*"
    },
    "string": {
        "type": "inline",
        "id_type": "text",
        "search_regex": '"{id}.*"'
    },
    "sim": {
        "type": "inline",
        "id_type": "snake_case",
        "search_regex": ":{id}\w*"
    },
    "rig": {
        "type": "inline",
        "id_type": "text",
        "search_regex": "\/{id}.*\/
    }"
    "list": {
        "type": "inline,block",
        "id_type": "snake_name",
        "search_regex": "\(\w\+\)\@<!\([$\|\[{id}.*\]\)"
    },
    "object list": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "Array\.new(.*)"
    },
    "hash": {
        "type": "inline,block",
        "id_type": "snake_name",
        "search_regex": "\(#\|-> \|\w\+\((.*)\)\? \)\@<!\({$\|{{id}.*}\)"
    },
    "object hash": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "Hash\.new(.*)"
    },
    "set": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "Set\.new(.*)"
    },
    "lambda": {
        "type": "inline",
        "id_type": "none",
        "search_regex": "-> {.*}"
    },
    "range": {
        "type": "inline",
        "id_type": "string_number",
        "search_regex": "({id}\d*..)"
    },
    "range to": {
        "type": "inline",
        "id_type": "string_number",
        "search_regex": "(\.\.{id}\d*)"
    },
    "range by": {
        "type": "inline",
        "id_type": "string_number",
        "search_regex": "(\.\.{id}\d*)"
    },
    "range until": {
        "type": "inline",
        "id_type": "string_number",
        "search_regex": "(\.\.\.{id}\d*)"
    },
    "interpol": {
        "type": "inline",
        "id_type": "snake_case",
        "search_regex": "#{{{id}.\{-}}}"
    },
    "key": {
        "type": "inline",
        "id_type": "snake_case",
        "search_regex": f"{{id}}\w*: \({VALUE_REGEX}, \ze\|{VALUE_REGEX\ze[}|]\)",
        "name_regex": f"{{id}}\w*\ze: {VALUE_REGEX}\+\(, \|[}\]\)",
        "body_regex": f"{{id}}\w*: \zs{VALUE_REGEX}\+\ze\(, \|[}|]\)"
    },
    "string key": {
        "type": "inline",
        "id_type": "snake_case",
        "search_regex": f'"{{id}}\w*": \({VALUE_REGEX}, \ze\|{VALUE_REGEX\ze[}|]\)',
        "name_regex": f'"{{id}}\w*"\ze: {VALUE_REGEX}\+\(, \|[}\]\)',
        "body_regex": f'"{{id}}\w*": \zs{VALUE_REGEX}\+\ze\(, \|[}|]\)'
    },
    "object key": {
        "type": "inline",
        "id_type": "snake_case",
        "search_regex": f"{{id}}\w* => \({VALUE_REGEX}, \ze\|{VALUE_REGEX\ze[}|]\)",
        "name_regex": f"{{id}}\w*\ze => {VALUE_REGEX}\+\(, \|[}\]\)",
        "body_regex": f"{{id}}\w* => \zs{VALUE_REGEX}\+\ze\(, \|[}|]\)"
    }
}
