from talon import Module

mod = Module()
mod.tag("code_comments", desc="")

@mod.action_class
class Actions:
    def code_comment_with_text(text: str):
        """Comment with text"""

    def code_comment():
        """Comment"""

    def code_line_comment_with_text(text: str):
        """Inline comment with text"""

    def code_line_comment():
        """Inline comment"""

    def code_multiline_comment_with_text(text: str):
        """Multiline comment with text"""

    def code_multiline_comment():
        """Multiline comment"""
