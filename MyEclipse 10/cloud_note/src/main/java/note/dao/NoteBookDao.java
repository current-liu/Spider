package note.dao;

import java.util.List;

import note.entity.NoteBook;

public interface NoteBookDao {
	public List<NoteBook> findByUserId(String userId);
	public void addBook(NoteBook noteBook);
	public void deleteBook(String bookId);
	public NoteBook findById(String id);

}
