CLASS_NAME_REGEX = "\(::\)\?\w\+\(::\w\+\)*"

RUBY_CLASSES_TOKENS = {
    "class": {
        "id_type": "class_name",
        "body": "block",
        "search_regex": f"class {{id}}{CLASS_NAME_REGEX}",
        "name_regex": f"class \zs{{id}}{CLASS_NAME_REGEX}\ze"
    },
    "superclass": {
        "id_type": "class_name",
        "body": "none",
        "search_regex": f"class {CLASS_NAME_REGEX}\zs < {{id}}{CLASS_NAME_REGEX}",
        "name_regex": f"class {CLASS_NAME_REGEX} < \zs{{id}}{CLASS_NAME_REGEX}"
    },
    "self class": {
        "id_type": "none",
        "body": "block",
        "search_regex": "class << self"
    },
    "class init": {
        "id_type": "none",
        "body": "block",
        "search_regex": "def initialize"
    },
    "private": {
        "id_type": "none",
        "body": "line",
        "search_regex": "private\( .*\)\?",
        "body_regex": "private \zs.*"
    },
    "protected": {
        "id_type": "none",
        "body": "line",
        "search_regex": "protected\( .*\)\?",
        "body_regex": "protected \zs.*"
    },
    "public": {
        "id_type": "none",
        "body": "line",
        "search_regex": "public\( .*\)\?",
        "body_regex": "public \zs.*"
    },
    "new": {
        "id_type": "class_name",
        "body": "line",
        "search_regex": f"{{id}}{CLASS_NAME_REGEX}\.new\((.*)\)\?",
        "name_regex": f"\zs{id}{CLASS_NAME_REGEX}\ze\.new\((.*)\)\?",
        "body_regex": f"{id}{CLASS_NAME_REGEX}\.new\zs\((.*)\)\?\ze"
    }
}
