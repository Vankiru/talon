DEFAULT_VALUE_REGEX = "\([[:alnum:]_\"',\. @$\[\]{}()]\+\|:\w\+\)"

RUBY_ARGUMENTS_TOKENS = {
    "arts": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "({id}.*)",
        "body_regex": "(\zs{id}.*\ze)"
    }
    "barbs": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regexp": " |{id}.*|",
        "body_regex": " |\zs{id}.*\ze|"
    },
    "comma": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": ",[ |\\n]"
    },
    "list art": {
        "id_type": "snake_name",
        "body_type": "none",
        "search_regex": "\(*\)\@<!\*{id}\w*",
        "name_regex": "\(*\)\@<!\*\zs{id}\w*"
    },
    "hash art": {
        "id_type": "snake_name",
        "body_type": "none",
        "search_regex": "\*\*{id}\w*",
        "name_regex": "\*\*\zs{id}\w*"
    },
    "block art": {
        "id_type": "snake_name",
        "body_type": "none",
        "search_regex": "&{id\w*}",
        "name_regex": "&\zs{id}\w*\ze"
    },
    "default": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": f"{{id}}\w* = \({DEFAULT_VALUE_REGEX}, \ze\|{DEFAULT_VALUE_REGEX\ze[)|]\)",
        "name_regex": f"{{id}}\w*\ze = {DEFAULT_VALUE_REGEX}\+\(, \|[)\]\)",
        "body_regex": f"{{id}}\w* = \zs{DEFAULT_VALUE_REGEX}\+\ze\(, \|[)|]\)"
    },
    "key art": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": f"{{id}}\w*: \({DEFAULT_VALUE_REGEX}, \ze\|{DEFAULT_VALUE_REGEX\ze[)|]\)",
        "name_regex": f"{{id}}\w*\ze: {DEFAULT_VALUE_REGEX}\+\(, \|[)\]\)",
        "body_regex": f"{{id}}\w*: \zs{DEFAULT_VALUE_REGEX}\+\ze\(, \|[)|]\)"
    },
    "forward art": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "(\zs\.\.\.\ze)"
    },
}
