RUBY_STATEMENTS_REGEX = {
    "require": {
        "type": "none",
        "id_type": "none",
        "search_regex": 'require "{id}.*"'
    },
    "unbind": {
        "type": "none",
        "id_type": "none",
        "search_regex": "undef {id}"
    },
    "defined": {
        "type": "none",
        "id_type": "none",
        "search_regex": "defined?({id})
    },
    "art read": {
        "type": "none",
        "id_type": "none",
        "search_regex": "attr_reader "
    },
    "art write": {
        "type": "none",
        "id_type": "none",
        "search_regex": "attr_writer "
    },
    "art access": {
        "type": "none",
        "id_type": "none",
        "search_regex": "attr_accessor "
    },
}
