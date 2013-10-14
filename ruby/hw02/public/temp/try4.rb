class Class
  def attr_accessor_with_history(attr_name)
    attr_name = attr_name.to_s # make sure it's a string
    #attr_reader attr_name # create the attribute's getter
    #attr_reader attr_name+"_history" # create bar_history getter

    stri = %Q{
      # YOUR CODE HERE
      
      def #{attr_name}
        @#{attr_name} ||= [ nil ]
        return @#{attr_name}[ @#{attr_name}.length - 1 ]
      end
      
      def #{attr_name}=( val )
        @#{attr_name} ||= [ nil ]
	if #{attr_name} != val
	    @#{attr_name} << val
        end
      end
      
      def #{attr_name}_history
        @#{attr_name} ||= [ nil ]
        return @#{attr_name}
      end
    }
    #puts stri

    class_eval stri

  end
end


class X
end


puts "T E S T S"
X.attr_accessor_with_history( "aaa" )
a = X.new
a.aaa_history
a.aaa
a.aaa = "das"
a.aaa = "das"
a.aaa = "das"
a.aaa = "ddsa"
a.aaa = "ddsa"
a.aaa = nil
a.aaa = "dsss"
puts a.aaa_history
puts "-----------------"
puts a.aaa


