
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
	if ( @#{attr_name}.length < 2 )
            return nil
        end
        return @#{attr_name}[ 0..(@#{attr_name}.length-2) ]
      end
    }
    #puts stri

    class_eval stri

  end
end


