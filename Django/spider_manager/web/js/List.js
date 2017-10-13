$('section .option li').eq(2).addClass('active');
$.ajax({
	url:url_head + "get_spiders",
	type:"get",
	dateType:"json",
	success:function(result){
		var datas = result;
		console.log(datas);

		var  page = {
		    "pageId":"",
		    "data":null,
		    "maxshowpageitem":5,//最多显示的页码个数
		    "pagelistcount":10,//每一页显示的内容条数
		      "init":function(listCount,currentPage,options){
		      	this.data=options.data,
		      	this.pageId=options.id,
		    this.maxshowpageitem=options.maxshowpageitem,//最多显示的页码个数
		    this.pagelistcount=options.pagelistcount//每一页显示的内容条数
		    page.initPage(listCount,currentPage);
		  },
		  /**
		     * 初始化数据处理
		     * @param listCount 列表总量
		     * @param currentPage 当前页
		     */
		  "initPage":function(listCount,currentPage){
		        var maxshowpageitem = page.maxshowpageitem;
		        if(maxshowpageitem!=null&&maxshowpageitem>0&&maxshowpageitem!=""){
		            page.maxshowpageitem = maxshowpageitem;
		        }
		        var pagelistcount = page.pagelistcount;
		        if(pagelistcount!=null&&pagelistcount>0&&pagelistcount!=""){
		            page.pagelistcount = pagelistcount;
		        }   
		        page.pagelistcount=pagelistcount;
		        if(listCount<0){
		            listCount = 0;
		        }
		        if(currentPage<=0){
		            currentPage=1;
		        }
		     
		        page.setPageListCount(listCount,currentPage);
		   },
		    /**
		     * 初始化分页界面
		     * @param listCount 列表总量
		     */
		    "initWithUl":function(listCount,currentPage){
		        var pageCount = 1;
		        if(listCount>=0){
		            var pageCount = listCount%page.pagelistcount>0?parseInt(listCount/page.pagelistcount)+1:parseInt(listCount/page.pagelistcount);
		        }
		        var appendStr = page.getPageListModel(pageCount,currentPage);
		        $("#"+page.pageId).html(appendStr);
		    },
		    /**
		     * 设置列表总量和当前页码
		     * @param listCount 列表总量
		     * @param currentPage 当前页码
		     */
		    "setPageListCount":function(listCount,currentPage){
		        listCount = parseInt(listCount);
		        currentPage = parseInt(currentPage);
		        page.initWithUl(listCount,currentPage);
		        page.initPageEvent(listCount);
		        page.viewPage(currentPage,listCount,page.pagelistcount,page.data)
		//      fun(currentPage);
		    },
		    //页面显示功能
		     "viewPage":function (currentPage,listCount,pagelistcount,data){
		            var NUM=listCount%pagelistcount==0?listCount/pagelistcount:parseInt(listCount/pagelistcount)+1;
		            if(currentPage==NUM){
		                var result=data.slice((currentPage-1)* pagelistcount,data.length);
		            }
		            else{
		                var result=data.slice((currentPage-1)*pagelistcount,(currentPage-1)*pagelistcount+pagelistcount);
		            }
		            options.callBack(result);
		    },
		    "initPageEvent":function(listCount){
		        $("#"+page.pageId +">li[class='pageItem']").on("click",function(){
		            page.setPageListCount(listCount,$(this).attr("page-data"),page.fun);
		        });
		    },
		    "getPageListModel":function(pageCount,currentPage){
		        var prePage = currentPage-1;
		        var nextPage = currentPage+1;
		        var prePageClass ="pageItem";
		        var nextPageClass = "pageItem";
		        if(prePage<=0){
		            prePageClass="pageItemDisable";
		        }
		        if(nextPage>pageCount){
		            nextPageClass="pageItemDisable";
		        }
		        var appendStr ="";
		        appendStr+="<li class='"+prePageClass+"' page-data='1' page-rel='firstpage'>首页</li>";
		        appendStr+="<li class='"+prePageClass+"' page-data='"+prePage+"' page-rel='prepage'>&lt;上一页</li>";
		        var miniPageNumber = 1;
		        if(currentPage-parseInt(page.maxshowpageitem/2)>0&&currentPage+parseInt(page.maxshowpageitem/2)<=pageCount){
		            miniPageNumber = currentPage-parseInt(page.maxshowpageitem/2);
		        }else if(currentPage-parseInt(page.maxshowpageitem/2)>0&&currentPage+parseInt(page.maxshowpageitem/2)>pageCount){
		            miniPageNumber = pageCount-page.maxshowpageitem+1;
		            if(miniPageNumber<=0){
		                miniPageNumber=1;
		            }
		        }
		        var showPageNum = parseInt(page.maxshowpageitem);
		        if(pageCount<showPageNum){
		            showPageNum = pageCount;
		        }
		        for(var i=0;i<showPageNum;i++){
		            var pageNumber = miniPageNumber++;
		            var itemPageClass = "pageItem";
		            if(pageNumber==currentPage){
		                itemPageClass = "pageItemActive";
		            }
		
		            appendStr+="<li class='"+itemPageClass+"' page-data='"+pageNumber+"' page-rel='itempage'>"+pageNumber+"</li>";
		        }
		        appendStr+="<li class='"+nextPageClass+"' page-data='"+nextPage+"' page-rel='nextpage'>下一页&gt;</li>";
		        appendStr+="<li class='"+nextPageClass+"' page-data='"+pageCount+"' page-rel='lastpage'>尾页</li>";
		       return appendStr;
		
		    }
		}
		
		
		
		
		var options={
			"id":"page",//显示页码的元素
			"data":datas,//显示数据
		    "maxshowpageitem":3,//最多显示的页码个数
		    "pagelistcount":10,//每页显示数据个数
		    "callBack":function(result){
		    	var cHtml="<li><span>Name</span><span>简介</span><span>目标站点</span><span>项目</span><span>所在位置</span><span>状态</span><span>创建时间</span></li>";
		        for(var i=0;i<result.length;i++){
		        	var spiderid = result[i].pk;
		        	var name = result[i].fields.name;
		        	var intro = result[i].fields.intro;
		        	var target_site = result[i].fields.target_site;
		        	var project = result[i].fields.project;
		        	var loc = result[i].fields.loc;
		        	var type = result[i].fields.type;
		        	var create_time = result[i].fields.create_time.split('T')[0];
		        	
		        	cHtml+="<li data-id='"+spiderid+"'><span class='jump_info'>"+name+"</span><span><a href ='###' title='"+intro+"'>"+intro+"</a></span><span><a href ='javascript:return false;' title='"+target_site+"'>"+target_site+"</a></span><span>"+project+"</span><span>"+loc+"</span><span>"+type+"</span><span>"+create_time+"</span></li>";
					$("#demoContent").html(cHtml);
					$('.jump_info').click(function(){
			        	var Id = $(this).parent().attr("data-id");
			        	console.log(Id);
			        	localStorage.setItem('spiderId',Id);
			      		location.href="Info.html";
			        });
		       				    
		        }
		    	
		    }
		};
		page.init(datas.length,1,options);



	},
	error:function(XMLHttpRequest, textStatus, errorThrown) {
        console.log(XMLHttpRequest.status);
        console.log(XMLHttpRequest.readyState);
        console.log(textStatus);
    }
});