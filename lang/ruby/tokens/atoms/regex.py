content = "{id}.\{-}"
suffix = "\/[iomxneus]*"

prefix_1 = "\%(\%(^\|\<\%(and\|or\|while\|until\|unless\|if\|elsif\|when\|not\|then\|else\)\|[;\~=!|&(,{[<>?:*+-]\)\s*\)\@<=/"
prefix_2 = "\%(\w\+\s\+\)\@<=/\%(=\|\_s\)\@!"

regex_1 = f"{prefix_1}{content}{suffix}"
regex_2 = f"{prefix_2}{content}{suffix}"

object = "\<Regexp.new\>(.\{-})"

delimiter = "[^[:alnum:][:space:]]"
percent_general = f"%r\({delimiter}\){content}\1{suffix}"

percent_paren = f"%r({content}){suffix}"
percent_bracket = f"%r{{{content}}}{suffix}"
percent_square = f"%r\[{content}\]{suffix}"
percent_tag = f"%r<{content}>{suffix}"
