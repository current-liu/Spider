$(function(){
	clearMsg_note_title();
});

function loadNotes(){	
	//给笔记本li设置选中样式
	$("#book_list li a").removeClass("checked");
	$(this).children("a").addClass("checked");
	//获取bookId
	var bookId = $(this).data("bookId");
	addCookie("bookId",bookId,2);
	delCookie("noteId");
	console.log("bookId:"+bookId);
	//发送请求
	show_pc_part(2);
	loadNotes_ajax(bookId);
	
}

function loadNotes_ajax(bookId){
	$.ajax({
		url:schema_url+"/note/loadNotes.do",
		type:"post",
		data:{"bookId":bookId},
		dataType:"json",
		success:function(result){			
			
			console.log(result.data);
			if(result.status==0){				
				var notes = result.data;			
				//清除原有笔记列表
				$("#note_list").empty();
				for(var i=0;i<notes.length;i++){
					var noteId = notes[i].CN_NOTE_ID;//map类型转成的json属性名大写，wtf！
					var noteTitle = notes[i].CN_NOTE_TITLE;
					var noteStatusId = notes[i].CN_NOTE_STATUS_ID;
					
					//console.log(notes[i].cn_note_id);
					//console.log(notes[i].cn_note_title);
					//将拼成的笔记列表的li添加到笔记ul中
					var s_li = '<li class="online">';
					s_li+='<a  >';
					if(noteStatusId=="1"){						
						s_li+='<i class="fa fa-file-text-o"';
					} else if(noteStatusId=="3"){
						s_li+='<i class="fa fa-sitemap"';
					} else {
						
					}
					
					s_li+='title="online" rel="tooltip-bottom"></i>';
					s_li+=noteTitle;
					s_li+='<button type="button" class="btn btn-default btn-xs btn_position btn_slide_down"><i class="fa fa-chevron-down"></i></button>';
					s_li+='</a>';
					s_li+='<div class="note_menu" tabindex="-1">';
					s_li+='<dl>';
					s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_move" title="移动至..."><i class="fa fa-random"></i></button></dt>';
					s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_share" title="分享"><i class="fa fa-sitemap"></i></button></dt>';
					s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_delete" title="删除"><i class="fa fa-times"></i></button></dt>';
					s_li+='</dl>';
					s_li+='</div>';
					s_li+='</li>';
					var $li = $(s_li);
					$li.data("noteId",noteId);//给li绑定笔记Id
					$("#note_list").append($li);
					
				}
			}
		},
		error:function(){
			alert("加载笔记列表失败");
		}
		
	});
}

function loadNote(){
	$("#note_list a").removeClass("checked");
	 $(this).find("a").addClass("checked");
	 
	var noteId = $(this).data("noteId");
	addCookie("noteId",noteId,2);
	console.log("noteId:"+noteId);
	$.ajax({
		url:schema_url+"/note/loadNote.do",
		type:"post",
		data:{"noteId":noteId},
		datatype:"json",
		success:function(result){
			if(result.status==0){
				console.log(result);
				var title = result.data.CN_NOTE_TITLE;
				var body = result.data.CN_NOTE_BODY;
				
				
				console.log("noteTitle:"+title);
				console.log("noteBody:"+body);
				
				
				$("#input_note_title").val(title);
				um.setContent(body);
				//切换编辑区域与预览区域
				$("#pc_part_5").hide();
				$("#pc_part_3").show();
			}
			
		},
		error:function(){
			alert("加载笔记内容失败");
		}
		
		
	});
}

function addNote_checkBookId(){
	var bookId = getCookie("bookId");
	if(bookId==null){
		alert("请选择一个笔记本");
	} else {
		alertAddNoteWindow();
	}
}

function alertAddNoteWindow(){
	
	$(".opacity_bg").show();//显示背景
	$("#can").load("alert/alert_note.html",function(){
		$(".input_head").focus();
	});//显示对话框	
}

function addNote(){
	var noteTitle = $("#input_note").val().trim();
	var bookId = getCookie("bookId");
	if(noteTitle==""){
		alert("笔记标题不能为空");
		return;
	}
	
	$("#note_list a").removeClass("checked");
	
	$.ajax({
		url:schema_url+"/note/addNote.do",
		type:"post",
		data:{"noteTitle":noteTitle,"noteBody":"  ","bookId":bookId,"userId":userId},
		dateType:"json",
		success:function(result){
			if(result.status==0){
				closeAlertWindow();
				var noteId = result.data;
				var s_li = '<li class="online">';
				s_li+='<a  class="checked">';
				s_li+='<i class="fa fa-file-text-o"';
				s_li+='title="online" rel="tooltip-bottom"></i>';
				s_li+=noteTitle;
				s_li+='<button type="button" class="btn btn-default btn-xs btn_position btn_slide_down"><i class="fa fa-chevron-down"></i></button>';
				s_li+='</a>';
				s_li+='<div class="note_menu" tabindex="-1">';
				s_li+='<dl>';
				s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_move" title="移动至..."><i class="fa fa-random"></i></button></dt>';
				s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_share" title="分享"><i class="fa fa-sitemap"></i></button></dt>';
				s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_delete" title="删除"><i class="fa fa-times"></i></button></dt>';
				s_li+='</dl>';
				s_li+='</div>';
				s_li+='</li>';
				var $li = $(s_li);
				$li.data("noteId",noteId);//给li绑定笔记Id
				$("#note_list").prepend($li);
				//模拟点击刚添加的note
				note_listClick();
				addCookie("noteId",noteId,2);
				
			}
		},
		error:function(){
			alert("创建笔记失败");
		}
	});
}

function saveNote_check(){
//	var bookId = getCookie("bookId");	
//	var noteId = getCookie("noteId");
//	//TODO cookie在此处使用存在bug，当前没有note被选中，cookie里仍然有noteId值
	
	//根据class=checked来获取当前被选中li的id，比利用Cookie更为合理
	 var $li_n = //获取选中的笔记li元素
		 $("#note_list a.checked").parent();
	 var noteId = $li_n.data("noteId");
	 var $li_b = //获取选中的笔记li元素
		 $("#book_list a.checked").parent();
	 var bookId = $li_b.data("bookId");
	 
	if(noteId==null){
		if(bookId==null){
			console.log("saveNote_check():alert()");
			alert("选择一个笔记本后重新保存，以新建一份笔记");				
		} else {
			console.log("saveNote_check():save_AddNote()");
			save_AddNote(bookId);
		}
	} else {
		console.log("saveNote_check():saveNote()");
		console.log("noteId:"+noteId);
		saveNote(noteId,bookId,$li_n);
	}
} 

function saveNote(noteId,bookId,$li_n){
//	var noteId = getCookie("noteId");
//	var bookId = getCookie("bookId");
	var noteTitle = $("#input_note_title").val().trim();
	var noteBody = um.getContent();
			 
	//清除上次提示信息
//	$("#note_title_span").html("");
	if(noteTitle==""){
		$("#note_title_span").html("<font color='red'>标题不能为空</font>");
		return;
	}
	
	$.ajax({
		url:schema_url+"/note/updateNote.do",
		type:"post",
		data:{"noteId":noteId,"noteTitle":noteTitle,"noteBody":noteBody},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				//alert("保存笔记成功");
				//var msg = "保存笔记成功";
				alertMsgWindow("保存笔记成功");
				//更新列表li中标题
				var sli = "";
				sli+='<i class="fa fa-file-text-o" title="online" rel="tooltip-bottom"></i>';
				sli+= noteTitle;
				sli+='<button type="button" class="btn btn-default btn-xs btn_position btn_slide_down"><i class="fa fa-chevron-down"></i></button>';
				//将选中li元素的a内容替换
				$li_n.find("a").html(sli);
			}
		},
		error:function(){
			alert("保存笔记失败");
		}
		
	});
	
}

function save_AddNote(bookId){
	
//	var bookId = getCookie("bookId");
	var noteTitle = $("#input_note_title").val().trim();
	var noteBody = um.getContent();
	
	if(noteTitle==""){
		$("#note_title_span").html("<font color='red'>标题不能为空</font>");
		return;
	}
	
	$("#note_list a").removeClass("checked");
	
	$.ajax({
		url:schema_url+"/note/addNote.do",
		type:"post",
		data:{"noteTitle":noteTitle,"noteBody":noteBody,"bookId":bookId,"userId":userId},
		dateType:"json",
		success:function(result){
			if(result.status==0){
				closeAlertWindow();
				var noteId = result.data;
				var s_li = '<li class="online">';
				s_li+='<a class="checked">';
				s_li+='<i class="fa fa-file-text-o""';
				s_li+='title="online" rel="tooltip-bottom"></i>';
				s_li+=noteTitle;
				s_li+='<button type="button" class="btn btn-default btn-xs btn_position btn_slide_down"><i class="fa fa-chevron-down"></i></button>';
				s_li+='</a>';
				s_li+='<div class="note_menu" tabindex="-1">';
				s_li+='<dl>';
				s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_move" title="移动至..."><i class="fa fa-random"></i></button></dt>';
				s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_share" title="分享"><i class="fa fa-sitemap"></i></button></dt>';
				s_li+='<dt><button type="button" class="btn btn-default btn-xs btn_delete" title="删除"><i class="fa fa-times"></i></button></dt>';
				s_li+='</dl>';
				s_li+='</div>';
				s_li+='</li>';
				var $li = $(s_li);
				$li.data("noteId",noteId);//给li绑定笔记Id
				$("#note_list").prepend($li);
				
				//模拟点击刚添加的note
				note_listClick();
				
				addCookie("noteId",noteId,2);
			}
		},
		error:function(){
			alert("创建笔记失败");
		}
	});
	
}

/**
 * 重新点击标题输入框后，清除原有提示信息
 */
function clearMsg_note_title(){	
	$("#input_note_title").focus(function(){
		$("#note_title_span").html("");		
	});
}

function alertMsgWindow(msg){
	//console.log(msg);
	
	$("#can").load("alert/alert_msg.html",function(){
		$(".opacity_bg").show();//显示背景
		$("#msg_info").html(""+msg);
	});
	
}
/**
 * 模拟点击note
 * 筛选条件为 class=checked   
 */
function note_listClick(){
	var $li_n = //获取选中的笔记li元素
		 $("#note_list a.checked").parent();
	$li_n.click();
}

function deleteNote(){
	var $li = $("#note_list a.checked").parent();
	var noteId = $li.data("noteId");
	$.ajax({
		url:schema_url+"/note/deleteNote.do",
		type:"post",
		data:{"noteId":noteId},
		dataType:"json",
		success:function(result){
			alert(result.msg);
		},
		error:function(){
			alert("删除笔记失败");
		}
		
	});
}

function showNoteMenu(){
	//点击下拉按钮显示菜单
	$("#note_list").on("click",".btn_slide_down",function(){
		//console.log("showNoteMenu");
		//隐藏所有li的菜单
		$("#note_list .note_menu").hide();
		//将点击的li的菜单显示
		var $li = $(this).parents("li");
		var $menu = $li.find(".note_menu");
		$menu.slideDown(500);
		//将当前笔记li设置为选中
		$("#note_list a").removeClass("checked");
		$li.find("a").addClass("checked");
		//阻止冒泡
		return false;
	});
	//点击页面其他位置隐藏菜单
	$("body").click(function(){
		$("#note_list .note_menu").hide();
	});
	//当鼠标移开菜单时隐藏菜单
	$("#note_list").on("mouseout",".note_menu",function(){
		$(this).hide();
	});
	//当鼠标移上菜单时保持显示
   $("#note_list").on("mouseover",".note_menu",function(){
		$(this).show();
	});
};

function alertDeleteNote(){
	$(".opacity_bg").show();//显示背景
	$("#can").load("alert/alert_delete_note.html");//显示对话框		
}
/**
 * 笔记移至回收站
 */
function sureDeleteNote(){
	var $li = $("#note_list a.checked").parent();
	var noteId = $li.data("noteId");
	$.ajax({
		url:schema_url+"/note/updateStatusBin.do",
		type:"post",
		data:{"noteId":noteId},
		dataType:"json",
		success:function(result){
			//删除笔记li
			$li.remove();
			//清空笔记内容编辑区
			um.setContent("");
			$("#input_note_title").val("");
			alert(result.msg);			
		},
		error:function(){
			alert("删除笔记失败");
		}
		
	});
	
}

function alertMoveNote(){
	var bookId_old = $("#book_list a.checked").parent().data("bookId");
	$(".opacity_bg").show();//显示背景
	$("#can").load("alert/alert_move.html",function(){
		var books = $("#book_list li");
		for(var i=0;i<books.length;i++){
			var $li = $(books[i]);
			var bookId = $li.data("bookId");
			if (bookId==bookId_old){
				continue;
			}
			var bookName = $li.text().trim();
			var opt = '<option value="'+bookId+'">- '+bookName+' -</option>';
			$("#moveSelect").append(opt);
		}
		
	});//显示对话框		
}

function sureMoveNote(){
	var $li = $("#note_list a.checked").parent();
	var noteId = $li.data("noteId");	
	var bookId = $("#moveSelect").val();
	
	if(bookId=="none"){
		$("#select_span").html("请选择一个笔记本");
		return;
	}
	$.ajax({
		url:schema_url+"/note/updateBookId.do",
		type:"post",
		data:{"noteId":noteId,"bookId":bookId},
		dataType:"json",
		success:function(result){
			closeAlertWindow();//关闭对话框
			$li.remove();//移除笔记li
			um.setContent("");
			$("#input_note_title").val("");
			alert(result.msg);
		},
		error:function(){
			alert("移动笔记失败");
		}
	});
}

function shareNote(){
	var noteId = $(this).parents("li").data("noteId");
	$.ajax({
		url:schema_url+"/share/share.do",
		type:"post",
		data:{"noteId":noteId},
		dataType:"json",
		success:function(result){
			if(result.status==0 || result.status==1) {
				alert(result.msg);
//				$("#note_list .checked i:first").addClass("fa fa-sitemap");
//				$(this).find("a").addClass("checked");
				var icon = $("#note_list a.checked").parent().find("i:first");
				//改变title前小图标
				icon.removeClass("fa fa-file-text-o");
				icon.addClass("fa fa-sitemap");
			}
		},
		error:function(){
			alert("分享失败");
		}
		
		
	});
}

function searchNote(event){
//	var keyword = $("#search_note").val().trim();
	var keyword = $(this).val().trim();
	var code = event.keyCode;
	if(code==13){
		//清除原有搜索结果
		$("#share_list").empty();		
		//alert(keyword);
		$.ajax({
			url:schema_url+"/share/searchNote.do",
			type:"post",
			data:{"keyword":keyword},
			dataType:"json",
			success:function(result){
				if(result.status==0){
					var notes = result.data;
					for(var i=0;i<notes.length;i++){
						var shareId = notes[i].cn_share_id;
						var shareTitle = notes[i].cn_share_title;
						var s_li = '<li class="online">';
						s_li+='<a  >';
						s_li+='<i class="fa fa-file-text-o"';
						s_li+='title="online" rel="tooltip-bottom"></i>';
						s_li+=shareTitle;
						s_li+='<button type="button" class="btn btn-default btn-xs btn_position btn_slide_down"><i class="fa fa-star"></i></button>';
						s_li+='</a>';					
						s_li+='</li>';
						var $li = $(s_li);
						$li.data("shareId",shareId);
						$("#share_list").append($li);
						//显示搜索结果div
//						$("#pc_part_2").hide();
//						$("#pc_part_6").show();
						show_pc_part(6);
					}
				}
			},
			error:function(){
				alert("检索分享笔记失败");
			}
					
		});
	}
}

function viewShareNote(){
	$("#share_list a").removeClass("checked");
	$(this).find("a").addClass("checked");
	var shareId = $(this).data("shareId");
	$.ajax({
		url:schema_url+"/share/loadShareNote.do",
		type:"post",
		data:{"id":shareId},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				var share = result.data;
				$("#noput_note_title").html(share.cn_share_title);
				$("#noput_note_body").html(share.cn_share_body);
				//切换编辑区域与预览区域
				$("#pc_part_3").hide();
				$("#pc_part_5").show();
			}
			
		},
		error:function(){
			alert("预览分享笔记失败");
		}
			
		
	});
}

function loadBin(){
	
	$.ajax({
		url:schema_url+"/note/loadBin.do",
		type:"post",
		data:{"userId":userId},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				$("#bin_list").empty();
				var notes = result.data;
				for(var i=0;i<notes.length;i++){
					var noteId = notes[i].CN_NOTE_ID;
					var noteTitle = notes[i].CN_NOTE_TITLE;
					var bookId = notes[i].CN_NOTEBOOK_ID;
//					console.log(notes[i]);
//					console.log(bookId);
					var s_li = '<li class="disable"><a ><i class="fa fa-file-text-o" title="online" rel="tooltip-bottom"></i>'+noteTitle+' <button type="button" class="btn btn-default btn-xs btn_position btn_delete"><i class="fa fa-times"></i></button><button type="button" class="btn btn-default btn-xs btn_position_2 btn_replay"><i class="fa fa-reply"></i></button></a></li>';
					var $li = $(s_li);
					$li.data("noteId",noteId);
					$li.data("bookId",bookId);
					$("#bin_list").append($li);
				}
				show_pc_part(4);
			}			
		},
		error:function(){
			alert("加载回收站失败");
		}
	});
}

function loadBinNote(){
	var noteId = $(this).data("noteId");
	
//	console.log(bookId);
//	console.log(noteId);
	$("#bin_list a").removeClass("checked");
	$(this).find("a").addClass("checked");
	$.ajax({
		url:schema_url+"/note/loadNote.do",
		type:"post",
		data:{"noteId":noteId},
		datatype:"json",
		success:function(result){
			if(result.status==0){
				console.log(result);
				var title = result.data.CN_NOTE_TITLE;
				var body = result.data.CN_NOTE_BODY;
												
				$("#noput_note_title").html(title);
				$("#noput_note_body").html(body);
				//切换编辑区域与预览区域
				$("#pc_part_3").hide();
				$("#pc_part_5").show();
			}
			
		},
		error:function(){
			alert("加载笔记内容失败");
		}		
		
	});
}

function alertDeleteRollback(){
	$(".opacity_bg").show();//显示背景
	$("#can").load("alert/alert_delete_rollback.html");//显示对话框	
}
function sureDeleteRollback(){
	var $li = $("#bin_list a.checked").parent();
	var noteId = $li.data("noteId");
	$.ajax({
		url:schema_url+"/note/deleteNote.do",
		type:"post",
		data:{"noteId":noteId},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				//删除笔记li
				$li.remove();
				//清空笔记内容编辑区
				$("#noput_note_title").html("");
				$("#noput_note_body").html("");
				alert(result.msg);
			}			
		},
		error:function(){
			alert("删除笔记失败");
		}
		
	});
}

function alertReplay(){
	$(".opacity_bg").show();//显示背景
	$("#can").load("alert/alert_replay.html");//显示对话框	
}
function sureReplay(){
	var $li = $("#bin_list a.checked").parent();
	var noteId = $li.data("noteId");
	var bookId = $li.data("bookId");
	//console.log(bookId);
	$.ajax({
		url:schema_url+"/note/replayNote.do",
		type:"post",
		data:{"noteId":noteId,"bookId":bookId},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				//删除回收站记录li
				$li.remove();				
				alert(result.msg);
			}			
		},
		error:function(){
			alert("恢复笔记失败");
		}
		
	});
}

function hightSearch(){
	var title = $("#title").val().trim();
	var status = $("#status").val(); 
	var begin = $("#begin").val().trim();
	var end = $("#end").val().trim();
	
	$.ajax({
		url:schema_url+"/note/hightSearch.do",
		type:"post",
		data:{"title":title,"status":status,"begin":begin,"end":end},
		dataType:"json",
		success:function(result){
			
			if(result.status==0){
				$("#hightSearch_list").empty();
				var notes = result.data;
				for(var i=0;i<notes.length;i++){
					var noteId = notes[i].cn_note_id;
					var noteTitle = notes[i].cn_note_title;
					var createTime = notes[i].cn_note_create_time;
					console.log(result.data);
					var s_li = '<li>';
					s_li+='<a  >';					
					s_li+=noteId+" "+noteTitle;						
					s_li+='</a>';					
					s_li+='</li>';
					var $li = $(s_li);
					$li.data("noteId",noteId);
					$("#hightSearch_list").append($li);
					
				}
				alert(result.msg);
			}
		},
		error:function(){
			alert("检索失败");
		}				
	});
}