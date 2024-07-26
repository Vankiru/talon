from talon import Module

mod = Module()
mod.tag("code_data_types", desc="Commands for adding literals")

@mod.action_class
class Actions:
    def code_data_type_true():
        """True"""

    def code_data_type_false():
        """False"""

    def code_data_type_none():
        """None/nil"""

    def code_data_type_string(text: str):
        """Double quote string"""

    def code_data_type_empty_string():
        """Empty double quote string"""

    def code_data_type_quote_string(text: str):
        """Single quoted string"""

    def code_data_type_empty_quote_string():
        """Empty single quoted string"""

    def code_data_type_multiline_string(text: str):
        """Multiline string"""

    def code_data_type_empty_multiline_string():
        """Empty multiline string"""

    def code_data_types_string_interpolation(name: str):
        """String interpolation"""

    def code_data_types_empty_string_interpolation():
        """Empty string interpolation"""

    def code_data_type_list():
        """List/array"""

    def code_data_type_multiline_list():
        """Multiline list/array"""

    def code_data_type_object_list():
        """Class/method definition of list/array"""

    def code_data_type_hash():
        """Hash/dict"""

    def code_data_type_multiline_hash():
        """Multiline hash/dict"""

    def code_data_type_object_hash():
        """Class/method definition of hash/dict"""

    def code_data_type_key_value(key: str):
        """Hash/dict key: value"""

    def code_data_type_set():
        """Set"""
