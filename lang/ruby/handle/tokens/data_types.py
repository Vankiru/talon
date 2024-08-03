RUBY_DATA_TYPES_TOKENS = {
    "true": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "true"
    },
    "false": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "false"
    },
    "none": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "nil"
    },
    "nun": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "nil"
    },
    "string": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": '"{id}.*"'
    },
    "quote string": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "'{id}.*'"
    },
    "multi string": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": '"\n{id}.*"'
    },
    "doc string": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": "<<~DOC\n{id}.*"
    },
    "rig": {
        "id_type": "text",
        "body_type": "line",
        "search_regex": "\/{id}.*\/
    }"
    "list": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "\(\w\+\)\@<!\[{id}.*"
    },
    "object list": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "Array\.new(.*)"
    },
    "string list": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "%w\["
    },
    "sim list": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "%i\["
    },
    "hash": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "\([\w\+ |#]\)\@<!{"
    },
    "object hash": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "Hash\.new"
    },
    "set": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "Set\.new"
    },
    "lambda": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "-> {"
    },
    "number": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "{id}"
    },
    "range": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "({id}\d*..)"
    },
    "range to": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "(\.\.{id}\d*)"
    },
    "range by": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "(\.\.{id}\d*)"
    },
    "range until": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "(\.\.\.{id}\d*)"
    },
    "interpol": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "#{{{id}}}"
    },
    "sim": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": ":{id}"
    },
    "key": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "{id}: "
    },
    "string key": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": '"{id}": '
    },
    "object key": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "{id} => "
    }
}
