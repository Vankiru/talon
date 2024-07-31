RUBY_CLASSES_TOKENS = {
    "class": {
        "name": "class_name",
        "content": "block",
        "search_regex": "class {name}",
        "name_regex": "class \zs{name}\ze"
    },
    "superclass": {
        "name": "class_name",
        "content": "none",
        "search_regex": "class \(::\)\?\w\+\(::\w\+\)*\zs < {name}",
        "name_regex": "class \(::\)\?\w\+\(::\w\+\)* < \zs{name}"
    },
    "self class": {
        "name": "none",
        "content": "block",
        "search_regex": "class << self"
    },
    "class init": {
        "name": "expression",
        "content": "block",
        "search_regex": "def initialize",
        "search_regex": "def initialize\zs(.*)"
    },
    "private": {
        "name": "none",
        "content": "line",
        "search_regex": "private",
        "content_regex": "private \zs.*"
    },
    "protected": {
        "name": "none",
        "content": "line",
        "search_regex": "protected",
        "content_regex": "protected \zs.*"
    },
    "public": {
        "name": "none",
        "content": "line",
        "search_regex": "public",
        "content_regex": "public \zs.*"
    },
    "new": {
        "name": "class_name",
        "content": "line",
        "search_regex": "{name}\.new\((.*)\)\?",
        "name_regex": "\zs{name}\ze\.new\((.*)\)\?",
        "content_regex": "{name}\.new\zs\((.*)\)\?\ze"
    }
}
