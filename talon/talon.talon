title: /\w*\.talon (.*) - VIM/
-

# Talon comands for .talon files

new (talon |talent) <user.text>:
  user.vim_insert_mode("{text}:", "o")

(talon | talent) escape:
  user.vim_insert_mode("key(escape)", "o")

(talon | talent) (inter | enter):
  user.vim_insert_mode("key(enter)", "o")

(talon | talent) key <user.letters>:
  user.vim_insert_mode("key({letters})", "o")

(talon | talent) key <user.word>:
  user.vim_insert_mode("key({word})", "o")

(talon | talent) key:
  user.vim_insert_mode("key()", "o")
  insert("i")

(talon | talent) insert:
  user.vim_insert_mode("insert(\"\")", "o")
  insert("hi")

# Talon title contexts

(talon | talent) title:
  command = """
  title: /\w*\.talon (.*) - VIM/
  -

  """

  user.vim_insert_mode(command)

(talon | talent) title python:
  command = """
  title: /\w*\.py (.*) - VIM/
  -

  """

  user.vim_insert_mode(command)

(talon | talent) title ruby:
  command = """
  title: /\w*\.rb (.*) - VIM/
  -

  """

  user.vim_insert_mode(command)

