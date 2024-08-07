content = "\(.\|\n\)\{-}"

prefix = "\%(\w\|[]})?!\"']\)\@<!"

array = "{prefix}\[{content}\]"
object = "Array.new(.\{-})"

delimiter = "[^[:alnum:][:space:]]"
percent_general = f"%[wWiI]\({delimiter}\){content}\1"

percent_paren = f"%[wWiI]({content})"
percent_bracket = f"%[wWiI]{{{content}}}"
percent_square = f"%[wWiI]\[{content}\]"
percent_tag = f"%[wWiI]<{content}>"

