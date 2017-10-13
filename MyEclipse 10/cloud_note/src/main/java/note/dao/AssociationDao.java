package note.dao;

import java.util.List;

import note.entity.NoteBook;
import note.entity.User;

public interface AssociationDao {
	public User findUser(String id);
	public List<User> findAll();
	public List<NoteBook> findAllBooks();

}
