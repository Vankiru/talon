title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_comments

frozen string:
  insert("gg")
  user.vim_insert_mode("# frozen_string_literal: true", "O")

magic encode:
  insert("gg")
  user.vim_insert_mode("# encoding: ", "O")
  insert("a")

magic warn:
  insert("gg")
  user.vim_insert_mode("# warn_indent: true", "O")

magic share none:
  insert("gg")
  user.vim_insert_mode("# shareable_constant_value: none", "O")

magic share lit:
  insert("gg")
  user.vim_insert_mode("# shareable_constant_value: literal", "O")

magic share every:
  insert("gg")
  user.vim_insert_mode("# shareable_constant_value: experimental_everything", "O")

magic share copy:
  insert("gg")
  user.vim_insert_mode("# shareable_constant_value: experimental_copy", "O")

