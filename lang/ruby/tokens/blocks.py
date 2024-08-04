RUBY_BLOCKS_TOKENS = {
    "block": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": "\([while|until|for] .*\)\@<! do\( |.*|\)\?"
    },
    "line block": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "\w\+\((.*)\)\?\zs {\( |.*|\)\?.*}",
        "body_regex": "\w\+\((.*)\)\? {\( |.*|\)\? \zs.*\ze}"
    }
}
