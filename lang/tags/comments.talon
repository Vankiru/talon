tag: user.code_comments
-

remark <user.text>:
  user.code_comment_with_text(text)

remark:
  user.code_comment()

line remark <user.text>:
  user.code_line_comment_with_text(text)

line remark:
  user.code_line_comment()

multi remark <user.text>:
  user.code_multiline_comment_with_text(text)

multi remark:
  user.code_multiline_comment()
