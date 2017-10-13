$(function(){
	//给登录按钮追加单击处理
	$("#login").click(function(){
		//清除原有提示信息
		$("#count_span").html("");
		$("#password_span").html("");
		//获取请求参数
		var name = $("#count").val().trim();
		var password = $("#password").val().trim();
		//格式检查
		var check = true;//通过检查
		if(name==""){
			check = false;
			$("#count_span").html("用户名为空");
		}
		if(password==""){
			check = false;
			$("#password_span").html("密码为空");
		}
		//通过格式检查,再发送ajax请求
		if(check){
			$.ajax({
				url:schema_url+"/user/login.do",
				type:"post",
				data:{"name":name,"password":password},
				dataType:"json",
				success:function(result){
					//alert(result.status);
					if(result.status==0){		
						//获取用户ID，写入Cookie
						var userId = result.data;
						//alert(userId);
						addCookie("uid",userId,2);
						//进入edit.html
						window.location.href="edit.html";
					}else if(result.status==1){
						$("#count_span").html(result.msg);
					}else if(result.status==2){
						$("#password_span").html(result.msg);
					}
				},
				error:function(){					
					alert("登录失败");
					
				}
			});
		}
	});
});