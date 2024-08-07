content = "{id}\(.\|\n\)\{-}"

quote = f"[\\]\@<!'{content}[\\]\@<!'"
double = f'[\\]\@<!"{content}[\\]\@<!"'
grave = f"[\\]\@<!`{content}[\\]\@<!`"

delimiter = "[^[:alnum:][:space:]]"
percent_general = f"%[qQ]\({delimiter}\){content}\1"

percent_paren = f"%[qQ]({content})"
percent_bracket = f"%[qQ]{{{content}}}"
percent_square = f"%[qQ]\[{content}\]"
percent_tag = f"%[qQ]<{content}>"

heredoc = f"\(<<[-~]\?\(\w\+\)\)\n{content}\n\2"

# Regex.register("string", [quote, double, grave, heredoc, percent("[qQ"]))
