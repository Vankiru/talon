minus = "-\="
prefix = "\%(0[dD]\)\="
digits = "\d\+\%(_\d\+\)*"
exponent = "\%([eE][-+]\={digits}\)\="
suffix = "r\=i\="

decimal = f"{minus}\<{prefix}{digits}\%(\.{digits}\)\={exponent}{suffix}\>"
# decimal = f"-\=\<\%(0[dD]\)\=\d\+\%(_\d\+\)*\%(\.\d\+\%(_\d\+\)*\)\=\%([eE][-+]\=\d\+\%(_\d\+\)*\)\=r\=i\=\>"

hexadecimal = "{minus}\<0[xX]\x\+\%(_\x\+\)*{suffix}\>"
octal = "{minus}\<0[oO]\=\o\+\%(_\o\+\)*{suffix}\>"
binary = f"{minus}\<0[bB][01]\+\%(_[01]\+\)*{suffix}\>"

# Regex.register("number", [decimal, hexadecimal, octal, binary])
