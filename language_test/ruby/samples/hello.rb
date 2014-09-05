# coding: utf-8
require "rubygems"
require "ruby-pinyin"

Dir.chdir("E:\\naviinfo\\13spring_evfc\\地铁")
files = Array.new
mapping = {
	"北京市" => "beijing",
	"上海市" => "shanghai",
	"南京市" => "jiangsu",
	"哈尔滨市" => "heilongjiang"
}
puts mapping["北京市"]

if mapping["北京市"] == nil
	puts "hh" 	
end 

puts Dir.pwd.encode("utf-8")
str = "中国"
puts str

puts `dir /b`.encode("utf-8")
#puts Dir.entries().encode("utf-8")

## rename key => value 
#mapping.each {|key, value| File.rename(key, value)}

# puts `mv 北京市 #{mapping["北京市"]}`.encode("utf-8")

##1 * 2 * 3 * 4 = 24
puts (1..4).reduce(:*)

puts "1234".index("4")

cmPerInch = 2.54

height = Math.sqrt(576.0/356.0) * 16
dotNumber = 1920.0 / height

printf "height: %.2finch  %.2fcm\ndotNumber:%.2f\n", height, height*cmPerInch, dotNumber
puts 1/0.010629921259843
puts 0.39370078740157 * (1/0.010629921259843)
#0.27毫米=0.010629921259843英寸



