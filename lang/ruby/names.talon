title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_names

(bang | bank) <user.method_name>:
  user.vim_insert_mode("{method_name}!", "a")

plight <user.method_name>:
  user.vim_insert_mode("{method_name}?", "a")

(class | type) instance <user.variable_name>:
  user.vim_insert_mode("@@{variable_name}", "a")

pack <user.class_name>:
  user.vim_insert_mode("::{class_name}", "a")

global <user.variable_name>:
  user.vim_insert_mode("${variable_name}", "a")
