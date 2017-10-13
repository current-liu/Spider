package note.service;

import note.uitl.NoteResult;

public interface ShareService {
	public NoteResult share(String noteId);
	public NoteResult findById(String id);
	public NoteResult searchNote(String keyword);

}
