- [Arguments](#arguments)
- [Blocks](#blocks)
- [Classes](#classes)
- [Comments](#comments)
- [Controls](#controls)
- [Data Types](#data-types)
- [Exceptions](#exceptions)
- [Library](#library)
- [Methods](#methods)
- [Names](#names)
- [Operators](#operators)
- [Statements](#statements)

## Arguments

```ruby
# arts
()
# barbs
 ||
# left art
(
# right art
)
# comma
, 
# line comma
,\n
# default <name> [to]
name: 
# list art <name>
*name
# hash art <name>
**name
# key art <name>
name:
# block art <name>
&name
# forward art
...
```

## Blocks
```ruby
# block
 do
end

# line block
 {  }
```

## Classes

```ruby
# class <name>
class Name
end

# self class
class << self
end

# superclass <name>
 < Name

# class init
def initialize
end

# private
private
# protected
protected
# public
public

# new <name>
Name.new
```

## Comments

```ruby
# remark <text>
# text

# line remark <text>
<code> # text

# multi remark <text>
=begin
text
=end

# frozen string
# frozen_string_literal: true

# magic encode
# encoding: 

# magic warn
# warn_indent: true

# magic share none
# shareable_constant_value: none

# magic share lit
# shareable_constant_value: literal

# magic share every
# shareable_constant_value: experimental_everything

# magic share copy
# shareable_constant_value: experimental_copy
```

## Controls

```ruby
# if
if 
end

# else
else

# else if
elsif 

# unless
unless 
end

# leaf
 if 

# unleaf
 unless

# triplet
 ?  : 

# case
case 
end

# when
when 

# then
 then

# while
while  do
end

# until
until  do
end

# end while
begin
end while

# line while
 while

# line until
 until

# for <item> in <list>
for item in list do
end

# break
break
# break if
break if 
# next
next
# next if
next if 
```

## Data Types

```ruby
# true
true
# false
false
# none | nun
nil

# number <number> 
12
# number <number> point <number>
12.34

# string <text>
"text"
# quote string <text>
'text'
# multi string <text>
"
text
"
# interpol <name>
#{name}
# interpol
#{}
# doc string <text>
<<~DOC
text
DOC

# sim <name>
:name

# list
[]
# multi list
[
]
# object list
Array.new()
# string list
%w[]
# sim list
%i[]

# hash
{}
# multi hash
{
}
# object hash
Hash.new()
# key <key> to
key: 
# string key <key> to
"key": 
# object key <key> to
key => 

# set
Set.new()

# range <from> to <to>
(from..to)
# range <from> until <to>
(from...to)
# range <from>
(from..)
# range to <to>
(..to)
# range until <to>
(...until)
# object range <from> to <to>
Range.new(from, to)
# object range <from> until <to>
Range.new(from, to, true)

# rig <text>
/text/

# lambda
-> {  }
```

# Exceptions

```ruby
# raise <name>
raise Name

# error <name>
NameError

# begin
begin
end

# rescue
rescue
# rescue <name>
rescue Name
# rescue as <name>
rescue => name
# rescue <name> as <name>
rescue Name => name

# ensure
ensure
# retry
retry
```

## Library

```ruby
# print <text>
puts "text"
```

## Methods

```ruby
# met <name>
def name
end

# short met <name>
def <name> = 

# met bank | mukbang <name>
def name!
end

# met plight <name>
def name?
end

# return
return
# parent
super
# yeild
yield
# yeild self
yeild self

# call <name>
.name
# call bang <name>
.name!
# call plight <name>
.name?
# safe call <name>
&.name
```

## Names

```ruby
# name <name>
name
# bang <name>
name!
# plight <name>
name?

# instance <name>
@name
# type instance <name>
@@name

# self <name>
self.name

# const <name>
NAME

# type <name>
Name
# pack <name>
::Name

# global <name>
$name
```

## Operators

```ruby
# set to
 = 
# set <name> to
name = 

# plus
 + 
# minus
 - 
# multi
 * 
# divide
 / 
# modulus
 % 
# power
**

# plus equal
 += 
# minus equal
 -= 
# multi equal
 -= 
# divide equal
 /= 
# mod equal
 %= 
# power equal
 **= 

# equal
 == 
# not equal
 != 
# great
 > 
# lest
 < 
# great equal
 >= 
# lest equal
 <= 
# compare
 <=>
# test equal
 === 

# add | also
 && 
# or | either
 || 
# not
 !
# text add | also
 and 
# text or | either
 or 
# text not
 not

# index
[]
# inside
 in 
# match
 => 

# bit and
 & 
# bit or
 | 
# bit ex
 ^ 
# bit not
 ~ 
# bit left
 << 
# bit right
 >> 
```

## Statements

```ruby
# require <path>
require "path"

# alias <name> to <name>
alias name name

# unbind <name>
undef name

# defined <name>
defined?(name)

# art read
attr_reader 
# art write
attr_writter 
# art access
attr_accessor 
```
