from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_data_type_true():
        actions.user.vim_insert_mode("true", "a")

    def code_data_type_false():
        actions.user.vim_insert_mode("false", "a")

    def code_data_type_none():
        actions.user.vim_insert_mode("nil", "a")

    def code_data_type_string(text: str):
        actions.user.vim_insert_mode(f"\"{text}\"", "a")

    def code_data_type_empty_string():
        actions.user.vim_insert_mode("\"\"", "a")
        actions.insert("i")

    def code_data_type_quote_string(text: str):
        actions.user.vim_insert_mode(f"'{text}'", "a")

    def code_data_type_empty_quote_string():
        actions.user.vim_insert_mode("''", "a")
        actions.insert("i")

    def code_data_type_multiline_string(text: str):
        actions.user.vim_insert_mode(f"\"\n{text}\n\"", "a")

    def code_data_type_empty_multiline_string():
        actions.user.vim_insert_mode("\"\n\"", "a")
        actions.insert("O")

    def code_data_types_string_interpolation(text: str):
        actions.user.vim_insert_mode(f"#{{{text}}}", "a")

    def code_data_types_empty_string_interpolation():
        actions.user.vim_insert_mode("#{}", "a")
        actions.insert("i")

    def code_data_type_list():
        actions.user.vim_insert_mode("[]", "a")

    def code_data_type_multiline_list():
        actions.user.vim_insert_mode("[\n]")

    def code_data_type_object_list():
        actions.user.vim_insert_mode("Array.new()", "a")

    def code_data_type_hash():
        actions.user.vim_insert_mode("{}", "a")

    def code_data_type_multiline_hash():
        actions.user.vim_insert_mode("{\n}")

    def code_data_type_object_hash():
        actions.user.vim_insert_mode("Hash.new()", "a")

    def code_data_type_key_value(text: str):
        key = actions.user.formatted_text(text, "SNAKE_CASE")
        actions.user.vim_insert_mode(f"{key}: ", "a")

    def code_data_type_set():
        actions.user.vim_insert_mode("Set.new()", "a")
