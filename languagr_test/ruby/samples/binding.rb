class Demo
  def initialize(n)
    @secret = n
  end
  def get_binding
    return binding()
  end

  def show
  	puts @secret
  end
end

k1 = Demo.new(99)
b1 = k1.get_binding
k2 = Demo.new(-3)
b2 = k2.get_binding


puts eval("@secret", b1)   #=> 99
eval("@secret", b2)   #=> -3
eval("puts #{eval("@secret", b2)}")       #=> nil
eval("show", b1)