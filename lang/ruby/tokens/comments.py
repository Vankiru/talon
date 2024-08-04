RUBY_COMMENTS_TOKENS = {
    "remark": {
        "id_type": "text",
        "body_type": "line",
        "search_regex": "# {id}.*",
        "body_regex": "# \zs{id}.*"
    },
    "multi remark": {
        "id_type": "text",
        "body_type": "line",
        "search_regex": "=begin\n{id}.*",
        "body_regex": "=begin\n\zs{id}.*"
    },
    "frozen string": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "# frozen_string_literal: true"
    },
    "magic encode": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "# encoding: ",
        "body_regex": "# encoding: \zs.*"
    },
    "magic warn": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "# warn_indent: ",
        "body_regex": "# warn_indent: \zs.*"
    },
    "magic share": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "# shareable_constant_value: ",
        "body_regex": "# shareable_constant_value: \zs.*"
    },
    "magic share none": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "# shareable_constant_value: none"
    },
    "magic share lit": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "# shareable_constant_value: literal"
    },
    "magic share every": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "# shareable_constant_value: experimental_everything"
    },
    "magic share copy": {
        "id_type": "none",
        "body_type": "none",
        "search_regex": "# shareable_constant_value: experimental_copy"
    }
}
