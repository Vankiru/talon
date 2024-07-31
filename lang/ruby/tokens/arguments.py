RUBY_ARGUMENTS_TOKENS = {
    "arts": {
        "name": "none",
        "content": "line",
        "search_regex": "(.*)",
        "content_regex": "(\zs.\+\ze)"
    }
    "barbs": {
        "name": "none",
        "content": "line",
        "search_regexp": " |.*|",
        "content_regex": " |\zs.\+\ze|"
    },
    "comma": {
        "name": "none",
        "content": "none",
        "search_regex": ",[ |\\n]"
    },
    "line comma": {
        "name": "none",
        "content": "none",
        "search_regex": ",\n"
    },
    "default": {
        "name": "snake_name",
        "content": "line",
        "search_regex": "{name}\zs = \w*\ze\(, \|)\)",
        "content_regex": "{name} = \zs\w*\ze\(, \|)\)"
    },
    "list art": {
        "name": "none",
        "content": "line",
        "search_regex": "\(*\)\@<!\*{name}",
        "content_regex": "\(*\)\@<!\*\zs{name}"
    },
    "hash art": {
        "name": "none",
        "content": "line",
        "search_regex": "\*\*{name}",
        "content_regex": "\*\*\zs{name}"
    },
    "key art": {
        "name": "snake_name",
        "content": "line",
        "search_regex": "{name}:\( \w*\)\?\(, \|)\)",
        "name_regex": "{name}\ze:\( \w*\)\?\(, \|)\)",
        # ?
        "content_regex": "{name}:\( \zs\w*\ze\)\?\(, \|)\)"
    },
    "block art": {
        "name": "snake_name",
        "content": "none",
        "search_regex": "&{name}",
        "name_regex": "&\zs{name}\ze"
    },
    "forward art": {
        "name": "none",
        "content": "none",
        "search_regex": "(\zs\.\.\.\ze)"
    },
}
