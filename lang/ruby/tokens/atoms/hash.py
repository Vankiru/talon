content = "\(.\|\n\)\{-}"

prefix = "\%(->\s*\|{method_name}\|)\s*\|%[qQiIwWsr]\)\@<!"
hash = "{prefix}{{{content}}}"

object = "Hash.new(.\{-})"
