title: /.*\.py (.*) - VIM/
-

tag(): user.code_exceptions

try:
  user.vim_insert_mode("try:", "o")

except <user.class_name>:
  user.vim_insert_mode("except {class_name}:", "o")
  insert("h")

except <user.class_name> as <user.variable_name>:
  user.vim_insert_mode("except {class_name} as {variable_name}:", "o")

finally:
  user.vim_insert_mode("finally:", "o")

(raise | rise) <user.class_name> from <user.variable_name>:
  user.vim_insert_mode("raise {class_name} from {variable_name}", "o")

(raise | rise) <user.class_name> from (none | nun):
  user.vim_insert_mode("raise {class_name} from None", "o")
