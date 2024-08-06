RUBY_EXCEPTIONS_TOKENS = {
    "raise": {
        "type": "line",
        "id_type": "class_name",
        "search_regex": "raise {id}.*",
        "body_regex": "raise \zs{id}.*\ze",
    },
    "raise text": {
        "type": "line",
        "id_type": "text",
        "search_regex": 'raise "{id}.*"',
        "body_regex": 'raise "{id}.*"'
    },
    "rescue": {
        "type": "block",
        "id_type": "none",
        "search_regex": "rescue$"
    },
    "rescue": {
        "type": "block",
        "id_type": "class_name",
        "search_regex": "rescue {id}.*",
        "body_regex": "rescue \zs{id}.*\ze"
    },
    "rescue as": {
        "type": "block",
        "id_type": "snake_name",
        "search_regex": "rescue \(.* \)\?=> {id}.*"
        "body_regex": "rescue \zs\(.* \)\?=> {id}.*\ze"
    },
    "begin": {
        "type": "block",
        "id_type": "none",
        "search_regex": "begin$"
    },
    "ensure": {
        "type": "block",
        "id_type": "none",
        "search_regex": "ensure$"
    },
    "retry": {
        "type": "line",
        "id_type": "none",
        "search_regex": "retry$"
    }
}
