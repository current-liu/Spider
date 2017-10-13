package note.controller.share;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import note.service.ShareService;
import note.uitl.NoteResult;

@Controller
@RequestMapping("/share")
public class ShareController {
	@Resource
	private ShareService service;
		
	@RequestMapping("/share.do")
	@ResponseBody
	public NoteResult share(String noteId){
		//System.out.println(noteId);
		NoteResult result = service.share(noteId);
		return result;
		
	}
	@RequestMapping("/loadShareNote.do")
	@ResponseBody
	public NoteResult findById(String id){
		NoteResult result = service.findById(id);
		return result;
		
	}
	@RequestMapping("/searchNote.do")
	@ResponseBody
	public NoteResult searchNote(String keyword){
		NoteResult result = service.searchNote(keyword);
		return result;
	}
	
}
