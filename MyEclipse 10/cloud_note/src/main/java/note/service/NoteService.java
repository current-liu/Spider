package note.service;



import java.sql.Timestamp;

import note.uitl.NoteResult;

public interface NoteService {
	public NoteResult loadNotes(String bookId);
	public NoteResult loadNote(String id);
	public NoteResult addNote(String noteTitle,String noteBody,String bookId,String userId);
	public NoteResult updateNote(String noteId,String noteTitle,String noteBody);
	public NoteResult deleteNote(String id);
	public NoteResult updateStatusBin(String id);
	public NoteResult updateStatusNormal(String id,String bookId);
	public NoteResult updateBookId(String id,String bookId);
	public NoteResult loadBin(String userId);
	public NoteResult hightSearch(String title,String status,String begin,String end);
	

}
