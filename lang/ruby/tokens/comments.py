RUBY_COMMENTS_TOKENS = {
    "remark": {
        "name": "text",
        "content": "line",
        "search_regex": "^# {name}.*",
        "name_regex": "^# \zs{name}\ze.*",
        "context_regex": "^# \zs{name}.*"
    },
    "line remark": {
        "name": "text",
        "content": "line",
        "search_regex": ".* # {name}.*",
        "name_regex": ".* # \zs{name}\ze.*",
        "content_regex": ".* # \zs{name}.*"
    },
    "multi remark": {
        "name": "text",
        "content": "line",
        "search_regex": "=begin\n{name}.*",
        "search_regex": "=begin\n\zs{name}\ze.*",
        "search_regex": "=begin\n\zs{name}.*"
    },
    "frozen string": {
        "name": "none",
        "content": "none",
        "search_regex": "# frozen_string_literal: true"
    },
    "magic encode": {
        "name": "none",
        "content": "line",
        "search_regex": "# encoding: ",
        "content_regex": "# encoding: \zs.*"
    },
    "magic warn": {
        "name": "none",
        "content": "line",
        "search_regex": "# warn_indent: ",
        "content_regex": "# warn_indent: \zs.*"
    },
    "magic share": {
        "name": "none",
        "content": "line",
        "search_regex": "# shareable_constant_value: ",
        "content_regex": "# shareable_constant_value: \zs.*"
    },
    "magic share none": {
        "name": "none",
        "content": "none",
        "search_regex": "# shareable_constant_value: none"
    },
    "magic share lit": {
        "name": "none",
        "content": "none",
        "search_regex": "# shareable_constant_value: literal"
    },
    "magic share every": {
        "name": "none",
        "content": "none",
        "search_regex": "# shareable_constant_value: experimental_everything"
    },
    "magic share copy": {
        "name": "none",
        "content": "none",
        "search_regex": "# shareable_constant_value: experimental_copy"
    }
}
