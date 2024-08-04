RUBY_CONTROLS_TOKENS = {
    "if": {
        "id_type": "snake_name",
        "body_type": "inline,block",
        "search_regex": "\(^ *\zsif\|\zs if\) {id}.*",
        "test_regex": "\(^ *\zsif\|\zs if\) \zs{id}.*",
        "body_regex": "^ *\zs[^ ].*\ze if\ {id}.*"
    },
    "else": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": "else"
    },
    "else if": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "\zselsif {id}.*",
        "test_regex": "elsif \zs{id}.*"
    },
    "unless": {
        "id_type": "snake_name",
        "body_type": "inline,block",
        "search_regex": "\(^ *\zsunless\|\zs if\) {id}.*",
        "test_regex": "\(^ *\zsunless\|\zs if\) \zs{id}.*",
        "body_regex": "^ *\zs[^ ].*\ze unless\ {id}.*"
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
        "search_regex": "case {id}.*",
        "test_regex": "case \zs{id}.*"
    },
    "when": {
        "id_type": "none",
        "body_type": "block",
        "search_regex": "when {id}.*",
        "test_regex": "when \(\zs{id}.*\ze then .*\|\zs{id}.*$\)"
    },
    "then": {
        "id_type": "snake_name",
        "body_type": "inline,block",
        "search_regex": " then {id}.*",
        "body_regex": " then \zs{id}.*"
    },
    "while": {
        "id_type": "snake_name",
        "body_type": "inline,block",
        "search_regex": "\(^ *\zswhile\|\zs if\) {id}.*",
        "test_regex": "\(^ *\zswhile\|\zs if\) \zs{id}.*",
        "body_regex": "^ *\zs[^ ].*\ze while\ {id}.*"
    },
    "until": {
        "id_type": "snake_name",
        "body_type": "inline,block",
        "search_regex": "\(^ *\zsuntil\|\zs if\) {id}.*",
        "test_regex": "\(^ *\zsuntil\|\zs if\) \zs{id}.*",
        "body_regex": "^ *\zs[^ ].*\ze until\ {id}.*"
    },
    "end while": {
        "id_type": "snake_name",
        "body_type": "block",
        "search_regex": "end while {id}.*",
        "test_regex": "end while \zs{id}.*"
    },
    "break": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "break {id}.*",
        "body_regex": "break \(\zs{id}.*\ze&\|\zs{id}.*\ze \(if\|unless\) .*\)"
    },
    "next": {
        "id_type": "snake_name",
        "body_type": "line",
        "search_regex": "next {id}.*",
        "body_regex": "break \(\zs{id}.*\ze&\|\zs{id}.*\ze \(if\|unless\) .*\)"
    }
}
