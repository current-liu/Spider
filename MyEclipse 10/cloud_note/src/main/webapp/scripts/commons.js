$(function(){
	overwritingAlert();
	//focusOnInputHead();
});
/**
 * 首个输入框自动获取焦点
 */
function focusOnInputHead(){
	$(".input_head").focus();
	//$("#count").focus();
	console.log("focusOnInputHead");
}

function closeAlertWindow(){	
	$("#can").empty();
	$(".opacity_bg").hide();
	
}

//重写JS原生alert函数
function overwritingAlert(){
	window.alert=function(e){
		$('#can').load('./alert/alert_msg.html',function(){
			$('#msg_info').text(' '+e);
			$('.opacity_bg').show();
			//clearFocus();
//			$("#can").click(function(){
//				console.log("click");
//			});
//			$("#can").trigger("click");
//				
//			$("#can").keydown(function(event){
//				var code = event.keyCode;
//				if(code==13){
//					closeAlertWindow();
//				}
//				
//			});
		});
		$("#can").trigger("click");
		
		$("#can").keydown(function(event){
			var code = event.keyCode;
			if(code==13){
				closeAlertWindow();
			}
			
		});
		
		
	}
}
/**
 * note_list区域切换
 * @param id
 */
function show_pc_part(id){
//	全部笔记列表 pc_part_2
//	编辑笔记 pc_part_3
//	回收站笔记列表 pc_part_4
//	预览笔记 pc_part_5
//	搜索笔记列表 pc_part_6
//	收藏笔记列表 pc_part_7
//	参加活动的笔记列表 pc_part_8	
	
	$("#pc_part_2").hide();	
	$("#pc_part_4").hide();	
	$("#pc_part_6").hide();
	$("#pc_part_7").hide();
	$("#pc_part_8").hide();	
	
	switch(id){
	case 2:
		$("#pc_part_2").show();
		break;
	case 3:
		$("#pc_part_3").show();
		break;
	case 4:
		$("#pc_part_4").show();
		break;
	case 5:
		$("#pc_part_5").show();
		break;
	case 6:
		$("#pc_part_6").show();
		break;
	case 7:
		$("#pc_part_7").show();
		break;
	case 8:
		$("#pc_part_8").show();
		break;
	}
	
}