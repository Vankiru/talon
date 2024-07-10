from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_data_type_true():
        actions.user.vim_insert_mode(" True", "a")

    def code_data_type_false():
        actions.user.vim_insert_mode(" False", "a")

    def code_data_type_none():
        actions.user.vim_insert_mode(" None", "a")

    def code_data_type_string(text: str):
        actions.user.vim_insert_mode(f" \"{text}\"", "a")

    def code_data_type_quote_string(text: str):
        actions.user.vim_insert_mode(f" '{text}'", "a")

    def code_data_type_multiline_string(text: str):
        actions.user.vim_insert_mode(f" \"\"\"\n{text}\n\"\"\" ", "a")

    def code_data_type_list():
        actions.user.vim_insert_mode(" []", "a")

    def code_data_type_multiline_list():
        actions.user.vim_insert_mode(" [\n]", "a")

    def code_data_type_hash():
        actions.user.vim_insert_mode(" {}", "a")

    def code_data_type_multiline_hash():
        actions.user.vim_insert_mode(" {\n}")

    def code_data_type_set():
        actions.user.vim_insert_mode(" set()", "a")
