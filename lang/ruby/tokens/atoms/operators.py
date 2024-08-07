arithmetic = "+\|-\|\*\|\/\|%\|\*\*"
set = "=\|+=\|-=\|\*=\|\/=\|%=\|\*\*="
comparison = "==\|===\|!=\|>\|<\|>=\|<=\|<=>"
bool = "&&\|||\|\<and\>\|\<or\>\|\<not\>"
bitwise = "&\||\|^\|~\|<<\|>>"
match = "\<in\>\|=>"

negate = "\s\+!{value}"

operators = "\%(\s\+\%({arithemtic}\|{set}\|{comparison}\{bool}\|{bitwise}\|{match}\)\s\+\|{negate}\)

index = "\%([]})\"']\|{snake_name}\)\@<!\[.\{-1}\]"

