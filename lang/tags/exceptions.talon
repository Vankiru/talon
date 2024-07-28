tag: user.code_exceptions
-

(raise | rise) ({user.exception_name} | <user.class_name>):
  user.code_exception_raise(exception_name or class_name)

error ({user.exception_name} | <user.class_name>):
  user.vim_insert_mode("{user.exception_name or class_name}", "a")
