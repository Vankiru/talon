title: /.*\.rb (.*) - VIM/
-

print <user.text>:
  user.vim_insert_mode('puts "{text}"', "o")

print:
  user.vim_insert_mode("puts ", "o")

call {user.std_method}:
  user.vim_insert_mode(".{std_method}", "a")

(safe | save) (call | cold) {user.std_method}>:
  user.vim_insert_mode("&.{std_method}", "a")

(bang | bank) {user.std_method}:
  user.vim_insert_mode(".{std_method}!", "a")

plight {user.std_method}:
  user.vim_insert_mode(".{std_method}!", "a")
