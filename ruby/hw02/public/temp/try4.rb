class Class
  def attr_accessor_with_history(attr_name)
    attr_name = attr_name.to_s # make sure it's a string
    attr_reader attr_name # create the attribute's getter
    attr_reader attr_name+"_history" # create bar_history getter
    class_eval %Q{
      # YOUR CODE HERE
      @#{attr_name} = [ nil ]
      
      def #{attr_name}
        return @#{attr_name}[ @#{attr_name}.length - 1 ]
      end
      
      def #{attr_name}=( val )
        @#{attr_name} << val
      end
      
      def #{attr_reader}
        return @#{attr_name}
      end
    }
  end
end



