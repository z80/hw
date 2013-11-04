class AddDirectorToMovies < ActiveRecord::Migration
  def change
      reversible do |dir|
          change_table :movies do |m|
              dir.up   { m.add_column    :director, :string }
              dir.down { m.remove_column :director }
          end
      end
  end
end
