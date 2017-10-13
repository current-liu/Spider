package note.dao;

import java.util.List;
import java.util.Map;

import note.entity.Note;

public interface NoteDao {
		
	/**
	 * 数据库查询结果转成Map后，key为对应字段名-大写	 
	 */
	public Map<String,String> findById(String id);		
	public List<Map<String,String>> findByBookId(String bookId);	
	public void addNote(Note note);	
	public void updateNote(Note note);
	public void deleteNote(String id);	
	public void updateStatusBin(Note note);	
	public void updateStatusBin1(String id);
	public void updateStatusNormal(String id);
	public void updateStatusShare(String id);
	public void updateBookId(Map<String,String> m);
	public List<Map<String,String>> findBin(String userId);
	public List<Note> hightSearch(Map m);
		
}
