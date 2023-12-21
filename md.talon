title: /vim/
-

mark code <user.word>:
  key(escape)
  key(o)
  insert("```" + word)
  key(enter)
  insert("```")
  key(escape)
  key(k)
  key(p)
  
mark (three | tree):
  key(escape)
  key(o)
  insert("```sh")
  key(enter)
  key(enter)
  insert("```")
  key(up)
  key(super-v)
  key(escape)
  
mark title <user.text>:
  key(escape)
  key(o)
  insert("## ")
  user.insert_formatted(text, "CAPITALIZE_ALL_WORDS")
  key(escape)

mark subtitle <user.text>:
  key(escape)
  key(o)
  insert("### ")
  user.insert_formatted(text, "CAPITALIZE_ALL_WORDS")
  key(escape)

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
      integer id
    }}
  ```
  """

  key(o)
  insert(command)
  key(escape)

