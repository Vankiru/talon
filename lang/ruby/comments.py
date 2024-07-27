from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_comment_with_text(text: str):
        actions.user.vim_insert_mode(f"# {text}", "o")

    def code_comment():
        actions.user.vim_insert_mode("# ", "o")
        actions.insert("a")

    def code_line_comment_with_text(text: str):
        actions.insert("$")
        actions.user.vim_insert_mode(f" # {text}", "a")
        """Inline comment with text"""

    def code_line_comment():
        actions.insert("$")
        actions.user.vim_insert_mode(" # ", "a")
        actions.insert("a")

    def code_multiline_comment_with_text(text: str):
        actions.user.vim_insert_mode(f"=begin\n{text}\n=end", "o")

    def code_multiline_comment():
        actions.user.vim_insert_mode("=begin\n=end", "o")
        actions.insert("O")
