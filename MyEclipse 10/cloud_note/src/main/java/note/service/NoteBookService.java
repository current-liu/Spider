package note.service;


import note.uitl.NoteResult;

public interface NoteBookService {
	public NoteResult loadBooks(String userId);
	public NoteResult addBook(String bookName,String userId);
	public NoteResult deleteBook(String bookId);

}
