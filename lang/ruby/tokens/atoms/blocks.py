block = "\%([while|until|for].*\)\@<!\<do\>{barbs}\="

prefix = "\%(->\s*\|)\s*\|{method_name}\s*\)\@<="
line = "{prefix} {.\{-}}"

# -> {}
# ->() {}

# proc {}
# name {}
# name() {}

# name do |arg|
# end
 
# name(arg) do |arg|
# end
