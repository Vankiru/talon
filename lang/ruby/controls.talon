title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_controls

# if/unless/ternary

unless:
  user.vim_insert_mode("unless \nend", "o")
  insert("k$")

(line if) | leaf:
  user.vim_insert_mode(" if ", "a")

# unleaf is recognized as "and least" in a long phrase
(line unless) | unleaf:
  user.vim_insert_mode(" unless ", "a")

triplet:
  user.vim_insert_mode(" ?  : ", "a")
  insert("3h")

# case

case:
  user.vim_insert_mode("case \nend", "o")
  insert("k$")

when:
  user.vim_insert_mode("when ", "o")

then:
  user.vim_insert_mode(" then ", "a")

# while/until

until:
  user.vim_insert_mode("until  do\nend", "o")
  insert("k^el")

end while:
  user.vim_insert_mode("begin\nend while ", "o")

line while:
  user.vim_insert_mode(" while ", "a")

line until:
  user.vim_insert_mode(" until ", "a")

# break/next

break:
  user.vim_insert_mode("break", "o")

break if:
  user.vim_insert_mode("break if ", "o")

next:
  user.vim_insert_mode("next", "o")

next if:
  user.vim_insert_mode("next if ", "o")
