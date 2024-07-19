title: /\w*\.py (.*) - VIM/
-

anna <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("{variable}: ", "a")

anna <user.code_annotation_type> <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("{variable}: {code_annotation_type}", "a")

anna <user.code_annotation_type>:
  user.vim_insert_mode(": {code_annotation_type}", "a")

anna list <user.code_annotation_type>:
  user.vim_insert_mode(": list[{code_annotation_type}]", "a")

anna tuple <user.code_annotation_type>:
  user.vim_insert_mode(": tuple[{code_annotation_type}]", "a")
