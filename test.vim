let id = 'test'
let base = g:Ruby.atoms.base
let name = g:Ruby.atoms.name

let regex = #{body: '"name.snake_text"', token: '"\%(''".name.method_name."''\|->\s*\)\@<=(".body'}
let regex = map(regex, {_, value -> substitute(value, '\(\\\)\@<!"', "'", 'g')})

let key = 'body'
execute("let value = ".regex[key])
execute("let ".key." = ".value)
echo body

let key = 'token'
execute("let value = ".regex[key])
execute("let ".key." = ".value)
echo token

let text = '\%({base.method_name}\|->\s*\)\@<=({body}'
echo substitute(text, '{\w\+\%(\.\w\+\)\=}', 'submatch(0)')

echo substitute('\%({base.method_name}\|->\s*\)\@<=({body}', '{\w\+\%(\.\w\+\)\=}', '\="#".submatch(0)', '')
echo substitute('\%({base.method_name}\|->\s*\)\@<=({body}', '{\(\w\+\%(\.\w\+\)\=\)}', {match -> "'.".match[1].".'"}, '')






let base = g:Ruby.atoms.base
let tags = g:Ruby.atoms.tags

let regex = #{body: '{tags.snake_text}', token: '\%({base.method_name}\|->\s*\)\@<=({body}'}

let key = 'body'
let pat = '{\(\w\+\%(\.\w\+\)\=\)}'
let Sub = {match -> "'.".match[1].".'"}

let result = substitute(regex[key], pat, Sub, 'g')
let result = "'".result."'"

execute('let '.key.' = '.result)
