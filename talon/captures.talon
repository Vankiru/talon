title: /VIM/
-

# Captures

capture letter:
  user.vim_insert_mode(" <user.letter>")
  
capture letters:
  user.vim_insert_mode(" <user.letters>")

capture word:
  user.vim_insert_mode(" <user.word>")
  
capture text:
  user.vim_insert_mode(" <user.text>")

capture number:
  user.vim_insert_mode(" <user.number_string>")

capture anna:
  user.vim_insert_mode(" <user.code_annotation_type>")

capture key:
  user.vim_insert_mode(" <user.key_name>")

capture variable:
  user.vim_insert_mode(" <user.variable_name>")

capture met:
  user.vim_insert_mode(" <user.method_name>")

capture const:
  user.vim_insert_mode(" <user.const_name>")

capture class:
  user.vim_insert_mode(" <user.class_name>")
