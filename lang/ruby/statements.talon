title: /.*\.rb (.*) - VIM/
-

require <user.file_path>:
  user.vim_insert_mode('require "{file_path}"', "o")

alias <user.method_name> to <user.method_name>:
  user.vim_insert_mode("alias {method_name_1} {method_name_2}", "o")

unbind <user.method_name>:
  user.vim_insert_mode("undef {method_name}", "o")

defined <user.method_name>:
  user.vim_insert_mode("defined?({method_name})", "a")

defined:
  user.vim_insert_mode("defined?()", "a")
  insert("h")

art read:
  user.vim_insert_mode("attr_reader ", "o")

art (write | right):
  user.vim_insert_mode("attr_writer ", "o")

art (access | axis):
  user.vim_insert_mode("attr_accessor ", "o")
