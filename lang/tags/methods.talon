tag: user.code_methods
-

(met | meth) <user.method_name>:
  user.code_method_with_name(method_name)

(met | meth):
  user.code_method()

short (met | meth) <user.method_name>:
  user.code_short_method_with_name(method_name)

short (met | meth):
  user.code_short_method()

return:
  user.code_method_return()

(call | cold) <user.method_name>:
  user.code_method_call(method_name)
