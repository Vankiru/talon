RUBY_CONTROLS_TOKENS = {
    "if": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zsif",
        "name_regex": "^ *if\zs.*"
    },
    "else": {
        "name": "none",
        "content": "block",
        "search_regex": "else"
    },
    "else if": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zselsif",
        "name_regex": "^ *elsif\zs.*"
    },
    "unless": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zsunless",
        "name_regex": "^ *unless\zs.*"
    },
    "leaf": {
        "name": "expression",
        "content": "line",
        "search_regex": ".*\w.*\zs if",
        "name_regex": ".*\w.*\ if \zs.*",
        "content_regex": " *\zs.*\w.*\ze if"
    },
    "unleaf": {
        "name": "expression",
        "content": "line",
        "search_regex": ".*\w.*\zs unless",
        "name_regex": ".*\w.*\ unless \zs.*"
        "content_regex": " *\zs.*\w.*\ze unless"
    },
    "triplet": {
        "name": "expression",
        "content": "none",
        "search_regex": "? .* : .*",
        "name_regex": ".*\ze ? .* : .*"
    },
    "case": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zscase",
        "name_regex": "^ *case\zs.*"
    },
    "when": {
        "name": "none",
        "content": "block",
        "search_regex": "^ *\zswhen",
        # think about it
        "name_regex": "^ *when\zs.*\ze\(then .*\)\?"
    },
    "then": {
        "name": "none",
        "content": "line",
        "search_regex": " then ",
        "content_regex": " then \zs.*"
    },
    "while": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zswhile",
        "name_regex": "^ *while\zs.*"
    },
    "until": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zsuntil",
        "name_regex": "^ *until\zs.*"
    },
    "end while": {
        "name": "expression",
        "content": "block",
        "search_regex": "^ *\zsend while",
        "name_regex": "^ *end while\zs.*"
    },
    "line while": {
        "name": "expression",
        "content": "line",
        "search_regex": ".*\w.*\zs while",
        "name_regex": ".*\w.* while\zs.*"
        "content_regex": " *\zs.*\w.*\ze while.*"
    },
    "line until": {
        "name": "expression",
        "content": "line",
        "search_regex": ".*\w.*\zs until",
        "name_regex": ".*\w.* until\zs.*"
        "content_regex": " *\zs.*\w.*\ze until"
    },
    "break": {
        "name": "none",
        "content": "line",
        "search_regex": "break"
        "context_regex": "break \zs.*"
    },
    "break if": {
        "name": "expression",
        "content": "line",
        "search_regex": "break \(.* \)\?if"
        "name_regex": "break \(.* \)\?if\zs .*"
        "content_regex": "break \zs.*\ze if"
    },
    "next": {
        "name": "none",
        "content": "line",
        "search_regex": "next",
        "content_regex": "next\zs .*"
    },
    "next if": {
        "name": "expression",
        "content": "line",
        "search_regex": "next \(.* \)\?if"
        "name_regex": "next \(.* \)\?if\zs .*"
        "content_regex": "next \zs.*\ze if"
    },
}
