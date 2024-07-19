title: /\w*\.py (.*) - VIM/
-

tag(): user.code_names

reserve <user.text>:
  name = user.code_snake_case(text)
  user.vim_insert_mode("{name}_", "a")

mangle <user.text>:
  name = user.code_snake_case(text)
  user.vim_insert_mode("__{name}", "a")

package <user.text>:
  name = user.formatted_text(text, "NO_SPACES")
  user.vim_insert_mode(name, "a")
