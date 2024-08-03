title: /.*\.rb (.*) - VIM/
-

go next:
  user.vim_normal_mode("n")
  user.vim_command_mode("noh")

go (last | back):
  user.vim_normal_mode("N")
  user.vim_command_mode("noh")

# Go to

go [to] {user.nameless_token_regex}:
  user.code_go_to_token(nameless_token_regex)

go [to] {user.number_token_regex} <user.number_string>:
  user.code_go_to_token(number_token_regex, number_string)

go [to] {user.text_token_regex} <user.text>:
  user.code_go_to_token(text_token_regex, text)

go [to] {user.snake_name_token_regex} <user.snake_name>:
  user.code_go_to_token(snake_name_token_regex, snake_name)

go [to] {user.class_name_token_regex} <user.class_name>:
  user.code_go_to_token(class_name_token_regex, class_name)

go [to] {user.const_name_token_regex} <user.const_name>:
  user.code_go_to_token(const_name_token_regex, const_name)

go [to] {user.file_name_token_regex} <user.file_name>:
  user.code_go_to_token(file_name_token_regex, file_name)

go [to] <user.number_string>:
  user.code_go_to_token(number_string)

go [to] (<user.snake_name> | <user.class_name> | <user.const_name>):
  identifier = snake_name or class_name
  identifier = identifier or const_name
  user.code_go_to_token(identifier)

# Go back to

back [to] {user.nameless_token_regex}:
  user.code_back_to_token(nameless_token_regex)

back [to] {user.number_token_regex} <user.number_string>:
  user.code_back_to_token(number_token_regex, number_string)

back [to] {user.text_token_regex} <user.text>:
  user.code_back_to_token(text_token_regex, text)

back [to] {user.snake_name_token_regex} <user.snake_name>:
  user.code_back_to_token(snake_name_token_regex, snake_name)

back [to] {user.class_name_token_regex} <user.class_name>:
  user.code_back_to_token(class_name_token_regex, class_name)

back [to] {user.const_name_token_regex} <user.const_name>:
  user.code_back_to_token(const_name_token_regex, const_name)

back [to] {user.file_name_token_regex} <user.file_name>:
  user.code_back_to_token(file_name_token_regex, file_name)

back [to] <user.number_string>:
  user.code_back_to_token(number_string)

back [to] (<user.snake_name> | <user.class_name> | <user.const_name>):
  identifier = snake_name or class_name
  identifier = identifier or const_name
  user.code_back_to_token(identifier)

# Search

search {user.nameless_token_regex}:
  user.code_search_token(nameless_token_regex)

search {user.number_token_regex} <user.number_string>:
  user.code_search_token(number_token_regex, number_string)

search {user.text_token_regex} <user.text>:
  user.code_search_token(text_token_regex, text)

search {user.snake_name_token_regex} <user.snake_name>:
  user.code_search_token(snake_name_token_regex, snake_name)

search {user.class_name_token_regex} <user.class_name>:
  user.code_search_token(class_name_token_regex, class_name)

search {user.const_name_token_regex} <user.const_name>:
  user.code_search_token(const_name_token_regex, const_name)

search {user.file_name_token_regex} <user.file_name>:
  user.code_search_token(file_name_token_regex, file_name)

search <user.number_string>:
  user.code_search_token(number_string)

search (<user.snake_name> | <user.class_name> | <user.const_name>):
  identifier = snake_name or class_name
  identifier = identifier or const_name
  user.code_search_token(identifier)

