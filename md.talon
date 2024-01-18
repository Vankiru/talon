title: /vim/
-

mark code <user.word>:
  user.vim_insert_mode("```{word}\n```", "o")
  user.vim_normal_mode("kp")
  
mark (three | tree):
  user.vim_insert_mode("```sh\n\n```", "o")
  key(up)
  key(super-v)
  key(escape)
  
mark title <user.text>:
  title = user.formatted_text(text, "CAPITALIZE_ALL_WORDS")
  command = "## {title}\n"

  user.vim_insert_mode(command, "o")

mark subtitle <user.text>:
  title = user.formatted_text(text, "CAPITALIZE_ALL_WORDS")
  command = "### {title}\n"

  user.vim_insert_mode(command, "o")

mark dedent <user.number_string> (line | lines):
  user.vim_normal_mode("^hh")
  key(ctrl-v)
  insert("{number_string}jlx")

mermaid table <user.text>:
  title = user.formatted_text(text, "CAPITALIZE_ALL_WORDS")
  table = user.formatted_text(text, "SNAKE_CASE")

  command = """
  ```
  ---
  title: {title}
  ---
  erDiagram
    {table} {{
      id integer
    }}
  ```
  """

  user.vim_insert_mode(command, "o")

mermaid (graph | graf):
  command = """
  ```
  graph TB
  a --> b
  ```
  """

  user.vim_insert_mode(command, "o")
