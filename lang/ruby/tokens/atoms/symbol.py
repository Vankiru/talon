standard = ":{id}\<\w*\>"

content = ".\{-}"

quote = ":'{content}'"
double = ':"{content}"'

delimiter = "[^[:alnum:][:space:]]"
percent_general = f"%s\({delimiter}\){content}\1"

percent_paren = f"%s({content})"
percent_bracket = f"%s{{{content}}}"
percent_square = f"%s\[{content}\]"
percent_tag = f"%s<{content}>"
