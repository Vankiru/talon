title: /.*\.rb (.*) - VIM/
-

(go [to] | next) {user.nameless_token_regex}:
  user.code_search_token(nameless_token_regex)

(go [to] | next) {user.number_token_regex} <user.number_string>:
  user.code_search_token(number_token_regex, number_string)

(go [to] | next) {user.text_token_regex} <user.text>:
  user.code_search_token(text_token_regex, text)

(go [to] | next) {user.snake_name_token_regex} <user.snake_name>:
  user.code_search_token(snake_name_token_regex, snake_name)

(go [to] | next) {user.class_name_token_regex} <user.class_name>:
  user.code_search_token(class_name_token_regex, class_name)

(go [to] | next) {user.const_name_token_regex} <user.const_name>:
  user.code_search_token(const_name_token_regex, const_name)

(go [to] | next) {user.file_name_token_regex} <user.file_name>:
  user.code_search_token(file_name_token_regex, file_name)
