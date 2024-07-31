RUBY_DATA_TYPES_TOKENS = {
    "true": {
        "name": "none",
        "content": "none",
        "search_regex": "true"
    },
    "false": {
        "name": "none",
        "content": "none",
        "search_regex": "false"
    },
    "none": {
        "name": "none",
        "content": "none",
        "search_regex": "nil"
    },
    "nun": {
        "name": "none",
        "content": "none",
        "search_regex": "nil"
    },
    "string": {
        "name": "none",
        "content": "none",
        "search_regex": '"{identifier}.*"'
    },
    "quote string": {
        "name": "none",
        "content": "none",
        "search_regex": "'{identifier}.*'"
    },
    "multi string": {
        "name": "none",
        "content": "none",
        "search_regex": '"\n{identifier}.*"'
    },
    "doc string": {
        "name": "none",
        "content": "none",
        "search_regex": "<<~DOC\n{identifier}.*"
    },
    "rig": {
        "name": "none",
        "content": "none",
        "search_regex": "\/{identifier}.*\/
    }"
    "list": {
        "name": "none",
        "content": "none",
        "search_regex": "\(\w\+\)\@<!\["
    },
    "object list": {
            "name": "none",
            "content": "none",
            "search_regex": "Array\.new"
        },
    "string list": {
            "name": "none",
            "content": "none",
            "search_regex": "%w\["
        },
    "sim list": {
            "name": "none",
            "content": "none",
            "search_regex": "%i\["
        },
    "hash": {
            "name": "none",
            "content": "none",
            "search_regex": "\([\w\+ |#]\)\@<!{"
        },
    "object hash": {
            "name": "none",
            "content": "none",
            "search_regex": "Hash\.new"
        },
    "set": {
            "name": "none",
            "content": "none",
            "search_regex": "Set\.new"
        },
    "lambda": {
            "name": "none",
            "content": "none",
            "search_regex": "-> {"
        },
    "number": {
            "name": "none",
            "content": "none",
            "search_regex": "{identifier}"
        },
    "range": {
            "name": "none",
            "content": "none",
            "search_regex": "({identifier}\d*..)"
        },
    "range to": {
            "name": "none",
            "content": "none",
            "search_regex": "(\.\.{identifier}\d*)"
        },
    "range by": {
            "name": "none",
            "content": "none",
            "search_regex": "(\.\.{identifier}\d*)"
        },
    "range until": {
            "name": "none",
            "content": "none",
            "search_regex": "(\.\.\.{identifier}\d*)"
        },
    "interpol": {
            "name": "none",
            "content": "none",
            "search_regex": "#{{{identifier}}}"
        },
    "sim": {
            "name": "none",
            "content": "none",
            "search_regex": ":{identifier}"
        },
    "key": {
            "name": "none",
            "content": "none",
            "search_regex": "{identifier}: "
        },
    "string key": {
            "name": "none",
            "content": "none",
            "search_regex": '"{identifier}": '
        },
    "object key": {
            "name": "none",
            "content": "none",
            "search_regex": "{identifier} => "
        },
}
