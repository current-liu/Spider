package note.dao;

import note.entity.User;

public interface UserDao {
	public User findByName(String name);
	public void regist(User u);
	public User findById(String id);
	
}
