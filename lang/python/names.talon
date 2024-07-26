title: /\w*\.py (.*) - VIM/
-

tag(): user.code_names

reserve <user.variable_name>:
  user.vim_insert_mode("{variable_name}_", "a")

mangle <user.variable_name>:
  user.vim_insert_mode("__{variable_name}", "a")

package <user.text>:
  name = user.formatted_text(text, "NO_SPACES")
  user.vim_insert_mode(name, "a")
