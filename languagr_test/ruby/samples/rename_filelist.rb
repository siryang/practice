# coding: utf-8
require "rubygems"

Dir.chdir("E:\\naviinfo\\13spring_evfc\\地铁")
files = Array.new
mapping = {
	"北京市" => "beijing",
	"上海市" => "shanghai",
	"南京市" => "jiangsu",
	"哈尔滨市" => "heilongjiang"
	# "大连市"	 => 
	# "天津市"	 =>
	# "广州市"	 =>
	# "成都市"	 =>
	# "昆明市"	 =>
	# "杭州市"	 =>
	# "武汉市"	 =>
	# "沈阳市"	 =>
	# "深圳市"	 =>
	# "苏州市"	 =>
	# "西安市"	 =>
	# "郑州市"	 =>
	# "重庆市"	 =>
	# "长春市"
	# "香港"
}
puts mapping["北京市"]
if mapping["北京市"] == nil
	puts "hh" 	
end 
puts Dir.pwd.encode("utf-8")

#puts `dir /b`.encode("utf-8")
#puts Dir.entries().encode("utf-8")
begin
	mapping.each {|key, value| File.rename(key, value)}
rescue Exception => e
	puts e
end

#File.rename("北京市", "beijing")
# puts "mv 北京市 #{mapping["北京市"]}"
# puts `mv 北京市 #{mapping["北京市"]}`.encode("utf-8")

def sayHello
	puts "Hello"
	puts "current function:" + String(__callee__)
	puts "dir:" + String(__dir__)
	puts "method:" + String(__method__)
end

puts "date:" + %x{date}.encode("utf-8")
# $?.exitstatus

sayHello


