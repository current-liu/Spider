package note.dao;

import java.util.List;

import note.entity.Share;

public interface ShareDao {
	public void share(Share share);
	public Share findById(String id);
	public Share findByNoteId(String noteId);
	public List<Share> findLikeTitle(String title);

}
