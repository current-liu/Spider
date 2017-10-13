package note.service;

import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import note.dao.NoteDao;
import note.dao.ShareDao;
import note.entity.Share;
import note.uitl.NoteResult;
import note.uitl.NoteUtil;

@Service
public class ShareServiceImpl implements ShareService{
	
	@Resource	
	private ShareDao dao;
	@Resource
	private NoteDao noteDao;

	
	public NoteResult share(String noteId) {
		NoteResult result = new NoteResult();		
		Share s = dao.findByNoteId(noteId);		
		if( s != null){
			result.setStatus(1);
			result.setData(s.getCn_share_id());
			result.setMsg("该笔记已经分享过了");			
			return result;
		}
		noteDao.updateStatusShare(noteId);
		Map<String,String> m = noteDao.findById(noteId);
		//System.out.println(m);
		Share share = new Share();
		String id = NoteUtil.createId();
		share.setCn_share_id(id);
		share.setCn_note_id(noteId);
		share.setCn_share_title(m.get("CN_NOTE_TITLE"));
		share.setCn_share_body(m.get("CN_NOTE_BODY"));
		
		//System.out.println(share);
		dao.share(share);
		result.setStatus(0);
		result.setData(share.getCn_share_id());
		result.setMsg("分享笔记成功");
		return result;
	}

	public NoteResult findById(String id) {
		NoteResult result = new NoteResult();
		Share share = dao.findById(id);
		result.setStatus(0);
		result.setData(share);
		result.setMsg("查询笔记成功");
		return result;
	}

	public NoteResult searchNote(String keyword) {
		NoteResult result = new NoteResult();
		if(keyword != null && !"".equals(keyword)){
			keyword = "%"+keyword+"%";
		} else {
			keyword = "%";
		}
		List<Share> list = dao.findLikeTitle(keyword);
		result.setStatus(0);
		result.setData(list);
		result.setMsg("检索分享笔记成功");
		return result;
	}

}
