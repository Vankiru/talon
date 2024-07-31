RUBY_BLOCKS_TOKENS = {
    "block": {
        "name": "expression",
        "content": "block",
        "search_regex": "\([while|until|for] .*\)\@<! do",
        "name_regex": "\([while|until|for] .*\)\@<! do\zs.\+"
    },
    "line block": {
        "name": "expression",
        "content": "line",
        "search_regex": "\w\+\zs {.*}",
        # matches the first space { code }
        "name_regex": "\w\+ {\zs\( |.*|\)\?\ze .*}",
        "content_regex": "\w\+ {\( |.*|\)\? \zs.*\ze}"
    }
}
