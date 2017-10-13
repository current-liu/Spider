$(function(){
	//给注册按钮追加单击处理
	$('#regist_button').click(function(){		
		 		
		//获取表单信息
		var name = $("#regist_username").val().trim();
		var nick = $("#nickname").val().trim();
		var regist_password = $("#regist_password").val().trim();
		var password = $("#final_password").val().trim();
		//TODO检测表单信息格式 
		/* var check = true;
		if(name == "") {
			check = false;
			get('warning_1.0').style.display='block';
		} */
		$('#regist_username').blur();
		/* if(nick == ""){
			check = false;
			get('warning_4').style.display='block';
		} */
		$("#nickname").blur();
		$("#regist_password").blur();
		$("#final_password").blur();
		/* if(password == ""){
			check = false;
			get('warning_3.1').style.display='block';
		} */
		//修补输入第二个密码，直接点击注册，无法触发onblur事件的bugs
		/* if(regist_password!=password){
			check = false;
			get('warning_3').style.display='block';
		} */
		//发送ajax请求
		if(get('warning_1').style.display == 'block'||get('warning_1.0').style.display == 'block'||get('warning_2').style.display == 'block'
				||get('warning_3').style.display == 'block'||get('warning_4').style.display == 'block'){
			alert("请核对您的注册信息");
			return;
		};
//		if(!check){
//			alert("请核对您的注册信息");
//			return;
//		}
		$.ajax({
			url:schema_url+"/user/regist.do",
			type:"post",
			data:{"name":name,"password":password,"nick":nick},
			dataType:"json",
			success:function(result){
				if(result.status==0){
					alert(result.msg);
					$("#back").click();//触发返回按钮的单击
				}
			},
			error:function(){
				alert("注册发生异常");
			}
		});
	});	
});
$(function(){
	//用户名检查、查重 
	$('#regist_username').blur(function(){
		var name = $("#regist_username").val().trim();
		if(name == "") {		
			get('warning_1.1').style.display='none';
			get('warning_1.0').style.display='block';
			return;
		}
		$.ajax({
			url:schema_url+"/user/checkName.do",
			type:"post",
			data:{"name":name,},
			dataType:"json",
			success:function(result){
				if(result.status==0){
					get('warning_1.1').style.display='block';					
				}else if(result.status==1){
					get('warning_1.1').style.display='none';
					get('warning_1').style.display='block';
				}
			},
			error:function(){
				alert("注册发生异常");
			}
		});
	});
});