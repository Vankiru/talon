VARIABLE_NAME_REGEX = "\w\+"

RUBY_METHODS_REGEX = {
    "met": {
        "type": "line,block",
        "id_type": "snake_name",
        "search_regex": "\(un\)\@<!def {id}.*",
        "name_regex": "\(un\)\@<!def \zs{id}\w*[!?]\?\ze\((.*)\)\?",
        "body_regex": "\(un\)\@<!def {id}\w*[!?]\?\((.*)\)\?"
    },
    "met bank": {
        "type": "none",
        "id_type": "none",
        "search_regex": "def {id}!",
    },
    "mukbang": {
        "type": "none",
        "id_type": "none",
        "search_regex": "def {id}!",
    },
    "met plight": {
        "type": "none",
        "id_type": "none",
        "search_regex": "def {id}?",
    },
    "call": {
        "type": "none",
        "id_type": "none",
        "search_regex": ".{id}",
    },
    "call bang": {
        "type": "none",
        "id_type": "none",
        "search_regex": ".{id}!",
    },
    "call plight": {
        "type": "none",
        "id_type": "none",
        "search_regex": ".{id}?",
    },
    "safe call": {
        "type": "none",
        "id_type": "none",
        "search_regex": "&.{id}",
    },
    "return": {
        "type": "none",
        "id_type": "none",
        "search_regex": "return",
    },
    "parent": {
        "type": "none",
        "id_type": "none",
        "search_regex": "super",
    },
    "yeild": {
        "type": "none",
        "id_type": "none",
        "search_regex": "yield",
    },
    "yeild self": {
        "type": "none",
        "id_type": "none",
        "search_regex": "yeild self",
    }
}
