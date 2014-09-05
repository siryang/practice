require 'rubygems'
require 'ruby-pinyin'
puts PinYin.of_string('姚尚朗').join(',')
puts PinYin.of_string('姚尚朗',true).join(',')
puts PinYin.permlink('姚尚朗')
puts PinYin.permlink('姚尚朗 is 我')

code, value = "5452 ḿ".split(' ')
 
print value