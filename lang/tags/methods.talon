tag: user.code_methods
-

(met | meth) <user.text>:
  user.code_method_with_name(text)

(met | meth):
  user.code_method()

short (met | meth) <user.text>:
  user.code_short_method_with_name(text)

short (met | meth):
  user.code_short_method()

return:
  user.code_method_return()

call <user.text>:
  user.code_method_call(text)
