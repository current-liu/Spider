function loadNoteBooks(){
	//加载笔记本列表
	$.ajax({
		url:schema_url+"/noteBook/loadBooks.do",
		type:"post",
		data:{"userId":userId},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				var books = result.data;//笔记本json集合
				//循环集合生成笔记本li列表
				for(var i=0;i<books.length;i++){
					var bookName = books[i].cn_notebook_name;
					var bookId = books[i].cn_notebook_id;
					//拼成li元素
					var s_li = '<li class="online"><a  >';
					s_li+='<i class="fa fa-book" title="online" rel="tooltip-bottom"></i>';
					s_li+=bookName+'</a></li>';
					//将s_li字符串转成jQuery对象，藏bookId
					var $li = $(s_li);
					$li.data("bookId",bookId);
					
					//将li添加到笔记本ul中
					$("#book_list").append($li);
					
				}
			}
		}
	});
}

function alertAddBookWindow(){
	
	$(".opacity_bg").show();//显示背景
	$("#can").load("alert/alert_notebook.html",focusOnInputHead);//显示对话框	
	
}

function addNoteBook(){

	//console.log("create");
	var bookName = $("#input_notebook").val().trim();
	if(bookName==""){
		alert("笔记本名不能为空");
		return;
	}
	
	$("#book_list li a").removeClass("checked");
	
	$.ajax({
		url:schema_url+"/noteBook/addBook.do",
		type:"post",
		data:{"bookName":bookName,"userId":userId},
		dataType:"json",
		success:function(result){
			if(result.status==0){
				//关闭对话框
				closeAlertWindow();
				//添加一个笔记本li
				var bookId = result.data;
				var s_li = '<li class="online"><a class="checked">';
				s_li+='<i class="fa fa-book" title="online" rel="tooltip-bottom"></i>';
				s_li+=bookName+'</a></li>';
				//将s_li字符串转成jQuery对象，藏bookId
				var $li = $(s_li);
				$li.data("bookId",bookId);
				//将li添加到笔记本ul中
				$("#book_list").prepend($li);
				
				//模拟点击刚添加的book
				loadNotes_ajax(bookId);
				//book_listClick();
				
				addCookie("bookId",bookId,2);
				
			}
			
		},
		error:function(){
			alert("创建笔记本失败");
		}
		
	});
}

/**
 * 模拟点击book 筛选条件为 class=checked
 *  
 */  
function book_listClick(){
	var $li_b = //获取选中的笔记li元素
		 $("#book_list a.checked").parent();
	$li_b.click();
}
