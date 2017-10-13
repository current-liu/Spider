package note.service;

import java.sql.Timestamp;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import note.dao.NoteBookDao;
import note.dao.NoteDao;
import note.dao.ShareDao;
import note.entity.Note;
import note.entity.NoteBook;
import note.uitl.NoteResult;
import note.uitl.NoteUtil;
@Service
public class NoteServiceImpl implements NoteService {
	
	@Resource
	private NoteDao noteDao;
	@Resource
	private ShareDao shareDao;
	@Resource
	private NoteBookDao bookDao;
	
	
	
	public NoteResult loadNotes(String bookId) {
		List<Map<String,String>> list = noteDao.findByBookId(bookId);
//		Share s = shareDao.findByNoteId(id);
//		if(s!=null){
//			m.put("share", "shared");
//		}
		
		NoteResult result = new NoteResult();
		result.setStatus(0);
		result.setMsg("查询笔记成功");
		result.setData(list);
		return result;
		
	}
	
	@SuppressWarnings("rawtypes")
	public NoteResult loadNote(String id){
		Map m = noteDao.findById(id);
		
//		String v1 = (String)m.get("CN_NOTE_TITLE");
//		String v2 = (String)m.get("CN_NOTE_BODY");
//		System.out.println(v1+","+v2);
//		if(v2==null){
//			m.put("CN_NOTE_BODY", "  ");
//		}
		
		NoteResult result = new NoteResult();
		result.setStatus(0);
		result.setMsg("查询笔记内容成功");
		result.setData(m);
		return result;
			
	}

	public NoteResult addNote(String noteTitle, String noteBody,String bookId, String userId) {
		NoteResult result = new NoteResult();
		Note note = new Note();
		String noteId = NoteUtil.createId();		
		note.setCn_note_id(noteId);
		note.setCn_notebook_id(bookId);
		note.setCn_user_id(userId);
		note.setCn_note_title(noteTitle);
		Timestamp time = new Timestamp(System.currentTimeMillis());
		note.setCn_note_create_time(time);
		note.setCn_note_last_modify_time(time);
		note.setCn_note_type_id("1");
		note.setCn_note_status_id("1");
		note.setCn_note_body(noteBody);
		
		noteDao.addNote(note);
		result.setStatus(0);
		result.setMsg("新建笔记成功");
		result.setData(noteId);
		return result;
	}

	public NoteResult updateNote(String noteId, String noteTitle, String noteBody) {
		NoteResult result = new NoteResult();
		Note note = new Note();			
		note.setCn_note_id(noteId);		
		note.setCn_note_title(noteTitle);
		note.setCn_note_body(noteBody);
		Timestamp time = new Timestamp(System.currentTimeMillis());
		note.setCn_note_last_modify_time(time);
		noteDao.updateNote(note);
		result.setStatus(0);
		result.setMsg("保存笔记成功");
		result.setData(noteId);
		return result;
	}

	public NoteResult deleteNote(String id) {
		NoteResult result = new NoteResult();
		noteDao.deleteNote(id);
		result.setStatus(0);
		result.setMsg("删除笔记成功");
		result.setData(id);
		return result;
	}

	public NoteResult updateStatusBin(String id) {
		NoteResult result = new NoteResult();
//		Note note = new Note();			
//		note.setCn_note_id(id);			
//		Timestamp time = new Timestamp(System.currentTimeMillis());
//		note.setCn_note_last_modify_time(time);
//		noteDao.updateStatusBin(note);
		noteDao.updateStatusBin1(id);
		result.setStatus(0);
		result.setMsg("笔记已移至回收站");
		result.setData(id);
		return result;
	}

	public NoteResult updateStatusNormal(String id,String bookId) {
		NoteResult result = new NoteResult();
		noteDao.updateStatusNormal(id);
		//noteDao.findById(id);
		NoteBook book = bookDao.findById(bookId);
		result.setStatus(0);
		result.setMsg("笔记已还原到: "+book.getCn_notebook_name());
		result.setData(id);
		return result;
	}

	public NoteResult updateBookId(String id, String bookId) {
		Map<String,String> m = new HashMap<String, String>();
		m.put("cn_note_id", id);
		m.put("cn_notebook_id", bookId);
		
		NoteResult result = new NoteResult();
		noteDao.updateBookId(m);
		result.setStatus(0);
		result.setMsg("笔记已移动");
		result.setData(m);//noteId和新的笔记本Id
		return result;
	}

	public NoteResult loadBin(String userId) {
		List<Map<String,String>> list = noteDao.findBin(userId);		
		NoteResult result = new NoteResult();
		result.setStatus(0);
		result.setMsg("查询回收站笔记成功");
		result.setData(list);
		return result;
	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public NoteResult hightSearch(String title, String status, String begin, String end) {
		Map m = new HashMap();
		if(title !=null && !"".equals(title)){			
			title = "%"+title+"%";
			m.put("title", title);
		}
		if(status != null && !"0".equals(status)){
			m.put("status", status);
		}		
		if(begin != null && !"".equals(begin)){
			m.put("beginDate", begin);
		}
		if(end !=null && !"".equals(end)){
			m.put("endDate", end);
		}
		List<Note> list = noteDao.hightSearch(m);
		NoteResult result = new NoteResult();
		result.setStatus(0);
		result.setData(list);
		result.setMsg("检索成功");
		return result;
	}

	

}
