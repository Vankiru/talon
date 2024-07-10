title: /VIM/
-

search <user.text>:
  text = user.formatted_text(text, "SNAKE_CASE")
  user.vim_normal_mode("/{text}")
  key(enter)

search drop:
  user.vim_command_mode("noh")
  
search next:
  user.vim_normal_mode("n")

search last:
  user.vim_normal_mode_key("shift-n")

