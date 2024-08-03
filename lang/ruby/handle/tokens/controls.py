RUBY_CONTROLS_TOKENS = {
    "if": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zsif {id}.*",
        "test_regex": "^ *if\zs{id}.*"
    },
    "else": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": "else"
    },
    "else if": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zselsif {id}.*",
        "test_regex": "^ *elsif\zs{id}.*$"
    },
    "unless": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zsunless",
        "test_regex": "^ *unless\zs.*"
    },
    "leaf": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": ".*\w.*\zs if",
        "test_regex": ".*\w.*\ if \zs.*",
        "body_regex": " *\zs.*\w.*\ze if"
    },
    "unleaf": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": ".*\w.*\zs unless",
        "test_regex": ".*\w.*\ unless \zs.*"
        "body_regex": " *\zs.*\w.*\ze unless"
    },
    "triplet": {
        "id_type": "snake_name",
        "body_type": "none",
        "search_regex": "? .* : .*",
        "test_regex": ".*\ze ? .* : .*"
    },
    "case": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zscase",
        "test_regex": "^ *case\zs.*"
    },
    "when": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": "^ *\zswhen",
        # think about it
        "test_regex": "^ *when\zs.*\ze\(then .*\)\?"
    },
    "then": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": " then ",
        "body_regex": " then \zs.*"
    },
    "while": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zswhile",
        "test_regex": "^ *while\zs.*"
    },
    "until": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zsuntil",
        "test_regex": "^ *until\zs.*"
    },
    "end while": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "^ *\zsend while",
        "test_regex": "^ *end while\zs.*"
    },
    "line while": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": ".*\w.*\zs while",
        "test_regex": ".*\w.* while\zs.*"
        "body_regex": " *\zs.*\w.*\ze while.*"
    },
    "line until": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": ".*\w.*\zs until",
        "test_regex": ".*\w.* until\zs.*"
        "body_regex": " *\zs.*\w.*\ze until"
    },
    "break": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "break"
        "context_regex": "break \zs.*"
    },
    "break if": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "break \(.* \)\?if"
        "test_regex": "break \(.* \)\?if\zs .*"
        "body_regex": "break \zs.*\ze if"
    },
    "next": {
        "id_type": "none",
        "body_type": "line",
        "search_regex": "next",
        "body_regex": "next\zs .*"
    },
    "next if": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "next \(.* \)\?if"
        "test_regex": "next \(.* \)\?if\zs .*"
        "body_regex": "next \zs.*\ze if"
    }
}
