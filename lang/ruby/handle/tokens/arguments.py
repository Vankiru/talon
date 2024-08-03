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
    "line comma": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": ",\n"
    },
    "default": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "{id}\w* = \w*\ze\(, \|)\)",
        "name_regex": "{id}\w*\ze = \w*\(, \|)\)",
        "body_regex": "{id}\w* = \zs\w*\ze\(, \|)\)"
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
    "key art": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "{id}\w*:\( \w*\)\?\(, \|)\)",
        "name_regex": "{id}\w*\ze:\( \w*\)\?\(, \|)\)",
        # ?
        "body_regex": "{id}:\( \zs\w*\ze\)\?\(, \|)\)"
    },
    "block art": {
        "id_type": "snake_name",
        "body_type": "none",
        "search_regex": "&{id\w*}",
        "name_regex": "&\zs{id}\w*\ze"
    },
    "forward art": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "(\zs\.\.\.\ze)"
    },
}
