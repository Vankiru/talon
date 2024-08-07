content = "\%(.\|\n\)\{-}"

args = "\%((.\{-})\)\="
barbs = "\%(\s*|.\{-}|\)\="

lambda = "->{args}\s*{{{content}}}"
proc = "proc\s*{{{barbs}{content}}}"
