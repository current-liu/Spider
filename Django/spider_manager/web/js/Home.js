$('section .option li').eq(0).addClass('active');
$('aside .list li .main dd').mouseover(function(){
    $(this).find('.topline').stop().animate({'width':'100%'},300);
    $(this).find('.rightline').stop().animate({'height':'100%'},300);
    $(this).find('.bottomline').stop().animate({'width':'100%'},300);
    $(this).find('.leftline').stop().animate({'height':'100%'},300);
});
$('aside .list li .main dd').mouseout(function(){
    $(this).find('.topline').stop().animate({'width':'0'},300);
    $(this).find('.rightline').stop().animate({'height':'0'},300);
    $(this).find('.bottomline').stop().animate({'width':'0'},300);
    $(this).find('.leftline').stop().animate({'height':'0'},300);
});

$('aside .list li .main dd').mouseover(function(){
    $(this).find('.icon').stop().animate({'top':'-2px'});
    $(this).find('p').stop().animate({'top':'2px'});
});
$('aside .list li .main dd').mouseout(function(){
    $(this).find('.icon').stop().animate({'top':'0'});
    $(this).find('p').stop().animate({'top':'0'});
});
    
//各状态爬虫数量
//运行的爬虫
$.ajax({
	url:url_head +"get_spider_group_on_status",
	type:"get",
	data: {"status":1},
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result.length);
		localStorage.setItem('status1',result.length);
	}
});
//暂停的爬虫
$.ajax({
	url:url_head +"get_spider_group_on_status",
	type:"get",
	data: {"status":2},
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result.length);
		localStorage.setItem('status2',result.length);
	}
});
//错误的爬虫
$.ajax({
	url:url_head +"get_spider_group_on_status",
	type:"get",
	data: {"status":3},
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result.length);
		localStorage.setItem('status3',result.length);
	}
});
//全部的爬虫
$.ajax({
	url:url_head +"get_spiders",
	type:"get",
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result.length);
		localStorage.setItem('status4',result.length);
		
	}
});
var status1 = localStorage.getItem("status1");
var status2 = localStorage.getItem("status2");
var status3 = localStorage.getItem("status3");
var status4 = localStorage.getItem("status4");
	
//运行的爬虫
$('aside .list .main dd').eq(0).children('p').eq(1).html(status1);
//暂停的爬虫
$('aside .list .main dd').eq(1).children('p').eq(1).html(status2);
//错误的爬虫
$('aside .list .main dd').eq(2).children('p').eq(1).html(status3);
//全部的爬虫
$('aside .list .main dd').eq(3).children('p').eq(1).html(status4);

//错误提示
var num = Number($('aside .list .main dd').eq(2).children('p').eq(1).text());
var audio=document.createElement("audio");
var box = document.getElementById('box');
box.appendChild(audio);
audio.src="9.mp3";
if(1>0){
	audio.play();	
	audio.addEventListener('ended',function(){
		var r=confirm('出现'+num+'个错误');
		if (r==true){
			localStorage.setItem('status','error');
			localStorage.setItem('val','出错的爬虫');
			location.href="Run.html";
		}else{
			console.log("You pressed Cancel!");
		}
	},false);
	
}	
	
//爬虫分类点击
var classify = $('aside .list li').eq(0).children('.main').children('dl').children('dd');
for(i=0;i<classify.length-1;i++){
	classify.eq(i).click(function(){
		var status = $(this).children('span').text();
		localStorage.setItem('status',status);
		var val = $(this).children('p').eq(0).text();
		localStorage.setItem('val',val);
		location.href="Run.html";
	});
}
classify.eq(3).click(function(){
	location.href="List.html";
});
	
//爬虫运行情况
var timeArr = [];
var runArr = [];
var pauseArr = [];
var errorArr = [];
$.ajax({
	url:url_head +"get_spider_num_group_by_date",
	type:"get",
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result);
		for(i=0;i<result[0].run.length;i++){
	    	var timeObj = result[0].run[i].d;
			var runObj = result[0].run[i].n;
			timeArr.push(timeObj);
			runArr.push(runObj);
			var pauseObj = result[2].pause[i].n;
			pauseArr.push(pauseObj);
			var errorObj = result[1].error[i].n;
			errorArr.push(errorObj);
	    }
		console.log(timeArr);
		console.log(runArr);
		console.log(errorArr);
		console.log(pauseArr);
			
		var myChartContentTop = echarts.init(document.getElementById('content-top'));
		var myChartContentTopoption = {
			
			title: {
		        text: '',
		        x: 'center'
		    },
		    tooltip: {
		        trigger: 'axis',
		        axisPointer: {
		            animation: false
		        }
		    },
		    legend: {
		        data:['run','pause','error'],
		        x: 'left'
		    },
		    axisPointer: {
		        link: {xAxisIndex: 'all'}
		    },
		    dataZoom: [
		        {
		            show: true,
		            realtime: true,
		            start: 30,
		            end: 70,
		            xAxisIndex: [0, 1]
		        },
		        {
		            type: 'inside',
		            realtime: true,
		            start: 30,
		            end: 70,
		            xAxisIndex: [0, 1]
		        }
		    ],
		    grid: [{
		        left: 50,
		        right: 50,
		        height: '50%'
		    }, {
		        left: 50,
		        right: 50,
		        height: '50%'
		    }],
		    xAxis : [
		        {
		            type : 'category',
		            boundaryGap : false,
		            axisLine: {onZero: true},
		            data: timeArr
		        },
		        {
		            gridIndex: 1,
		            type : 'category',
		            boundaryGap : false,
		            axisLine: {onZero: true},
		            data: timeArr
		        }
		    ],
		    yAxis : [
		        {
		            name : '',
		            type : 'value',
		            max : 100
		        },
		        {
		            gridIndex: 1,
		            name : '',
		            type : 'value',
		            max : 100
		        }
		    ],
		    series : [
		        {
		            name:'run',
		            type:'line',
		            symbolSize: 8,
		            hoverAnimation: false,
		            data: runArr
		        },
		        {
		            name:'pause',
		            type:'line',
		            symbolSize: 8,
		            hoverAnimation: false,
		            data: pauseArr
		        },
		        {
		            name:'error',
		            type:'line',
		            symbolSize: 8,
		            hoverAnimation: false,
		            data:errorArr
		        }
		    ]
		};
		myChartContentTop.setOption(myChartContentTopoption);
			

	},
	error:function(XMLHttpRequest, textStatus, errorThrown) {
        console.log(XMLHttpRequest.status);
        console.log(XMLHttpRequest.readyState);
        console.log(textStatus);
    }
});

//function Select(){
//	var objS = document.getElementById("select");
//	var grade = objS.options[objS.selectedIndex].innerHTML;
////	console.log(grade);
//	var type = objS.options[objS.selectedIndex].getAttribute("data-id");
////  console.log(type);
//
//	$.ajax({
//		url:url_head +"get_spider_num_group_by_date",
//		type:"get",
//		data: {"type":type},
//		async:true,
//		dateType:"json",
//		success:function(result){
//			console.log(result);
//			for(i=0;i<result[0].run.length;i++){
//		    	var timeObj = result[0].run[i].d;
//				var runObj = result[0].run[i].n;
//				timeArr.push(timeObj);
//				runArr.push(runObj);
//				var pauseObj = result[2].pause[i].n;
//				pauseArr.push(pauseObj);
//				var errorObj = result[1].error[i].n;
//				errorArr.push(errorObj);
//		    }
//			console.log(timeArr);
//			console.log(runArr);
//			console.log(errorArr);
//			console.log(pauseArr);
//				
//				var myChartContentTop = echarts.init(document.getElementById('content-top'));
//				var myChartContentTopoption = {
//					
//					title: {
//				        text: '',
//				        x: 'center'
//				    },
//				    tooltip: {
//				        trigger: 'axis',
//				        axisPointer: {
//				            animation: false
//				        }
//				    },
//				    legend: {
//				        data:['run','pause','error'],
//				        x: 'left'
//				    },
//				    axisPointer: {
//				        link: {xAxisIndex: 'all'}
//				    },
//				    dataZoom: [
//				        {
//				            show: true,
//				            realtime: true,
//				            start: 30,
//				            end: 70,
//				            xAxisIndex: [0, 1]
//				        },
//				        {
//				            type: 'inside',
//				            realtime: true,
//				            start: 30,
//				            end: 70,
//				            xAxisIndex: [0, 1]
//				        }
//				    ],
//				    grid: [{
//				        left: 50,
//				        right: 50,
//				        height: '50%'
//				    }, {
//				        left: 50,
//				        right: 50,
//				        height: '50%'
//				    }],
//				    xAxis : [
//				        {
//				            type : 'category',
//				            boundaryGap : false,
//				            axisLine: {onZero: true},
//				            data: timeArr
//				        },
//				        {
//				            gridIndex: 1,
//				            type : 'category',
//				            boundaryGap : false,
//				            axisLine: {onZero: true},
//				            data: timeArr
//				        }
//				    ],
//				    yAxis : [
//				        {
//				            name : '',
//				            type : 'value',
//				            max : 100
//				        },
//				        {
//				            gridIndex: 1,
//				            name : '',
//				            type : 'value',
//				            max : 100
//				        }
//				    ],
//				    series : [
//				        {
//				            name:'run',
//				            type:'line',
//				            symbolSize: 8,
//				            hoverAnimation: false,
//				            data: runArr
//				        },
//				        {
//				            name:'pause',
//				            type:'line',
//				            symbolSize: 8,
//				            hoverAnimation: false,
//				            data: pauseArr
//				        },
//				        {
//				            name:'error',
//				            type:'line',
//				            symbolSize: 8,
//				            hoverAnimation: false,
//				            data:errorArr
//				        }
//				    ]
//				};
//				myChartContentTop.setOption(myChartContentTopoption);
//				
//	
//		},
//		error:function(XMLHttpRequest, textStatus, errorThrown) {
//	        console.log(XMLHttpRequest.status);
//	        console.log(XMLHttpRequest.readyState);
//	        console.log(textStatus);
//	    }
//	});
//}
	

//爬虫类型
var dateObj = new Date();
var date = dateObj.getFullYear() + "-" + (dateObj.getMonth()+1) + "-" + (dateObj.getDate()-1);
console.log(date);

var typeArr = [1, 2, 3, 4, 5, 6];
var types = ['餐饮', '酒店', '景点', '购物', '娱乐', '交通'];
var hours = [];
var Arr1 = [];
var Arr2 = [];
var Arr3 = [];
var Arr4 = [];
var Arr5 = [];
var Arr6 = [];
$.ajax({
	url:url_head +"get_spider_num_group_by_hour",
	type:"get",
	data:{'date':date},
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result);
		//type1
		var Obj1 = result[0].d;
		for(i=0;i<Obj1.length;i++){
			var numObj1 = Obj1[i].n;
			var hour = Obj1[i].h;
			Arr1.push(numObj1);
			hours.push(hour);
		}
		console.log(hours);
		console.log(Arr1);
		//type2
		var Obj2 = result[1].d;
		for(i=0;i<Obj2.length;i++){
			var numObj2 = Obj2[i].n;
			Arr2.push(numObj2);
		}
		console.log(Arr2);
		//type3
		var Obj3 = result[2].d;
		for(i=0;i<Obj3.length;i++){
			var numObj3 = Obj3[i].n;
			Arr3.push(numObj3);
		}
		console.log(Arr3);
		//type4
		var Obj4 = result[3].d;
		for(i=0;i<Obj4.length;i++){
			var numObj4 = Obj4[i].n;
			Arr4.push(numObj4);
		}
		console.log(Arr4);
		//type5
		var Obj5 = result[4].d;
		for(i=0;i<Obj5.length;i++){
			var numObj5 = Obj5[i].n;
			Arr5.push(numObj5);
		}
		console.log(Arr5);
		//type6
		var Obj6 = result[5].d;
		for(i=0;i<Obj6.length;i++){
			var numObj6 = Obj6[i].n;
			Arr6.push(numObj6);
		}
		console.log(Arr6);
		
		Arr1 = Arr1.map(function (item) {
			return [0, item];
		});
		hours.forEach((c,i)=>{	Arr1[i].unshift(c);	});
		Arr2 = Arr2.map(function (item) {
			return [1, item];
		});
		hours.forEach((c,i)=>{	Arr2[i].unshift(c);	});
		Arr3 = Arr3.map(function (item) {
			return [2, item];
		});
		hours.forEach((c,i)=>{	Arr3[i].unshift(c);	});
		Arr4 = Arr4.map(function (item) {
			return [3, item];
		});
		hours.forEach((c,i)=>{	Arr4[i].unshift(c);	});
		Arr5 = Arr5.map(function (item) {
			return [4, item];
		});
		hours.forEach((c,i)=>{	Arr5[i].unshift(c);	});
		Arr6 = Arr6.map(function (item) {
			return [5, item];
		});
		hours.forEach((c,i)=>{	Arr6[i].unshift(c);	});
		
		Arr2.forEach((c,i)=>{	Arr1.push(c);	});
		Arr3.forEach((c,i)=>{	Arr1.push(c);	});
		Arr4.forEach((c,i)=>{	Arr1.push(c);	});
		Arr5.forEach((c,i)=>{	Arr1.push(c);	});
		Arr6.forEach((c,i)=>{	Arr1.push(c);	});
		
		
		var myChartContentMiddle = echarts.init(document.getElementById('content-middle'));
		var myChartContentMiddleoption = {
			title:{
		        text: '各时间段爬虫数量统计',
		        x: 'left',
		    },
		    tooltip: {
		        position: 'top'
		    },
		    animation: false,
		    grid: {
		        height: '50%',
		        y: '10%'
		    },
		    xAxis: {
		        type: 'category',
		        data: hours,
		        splitArea: {
		            show: true
		        }
		    },
		    yAxis: {
		        type: 'category',
		        data: types,
		        splitArea: {
		            show: true
		        }
		    },
		    visualMap: {
		        min: 0,
		        max: 10,
		        calculable: true,
		        orient: 'horizontal',
		        left: 'center',
		        bottom: '15%'
		    },
		    series: [{
		        name: 'Run',
		        type: 'heatmap',
		        data: Arr1,
		        label: {
		            normal: {
		                show: true
		            }
		        },
		        itemStyle: {
		            emphasis: {
		                shadowBlur: 10,
		                shadowColor: 'rgba(0, 0, 0, 0.5)'
		            }
		        }
		    }]
		};
		myChartContentMiddle.setOption(myChartContentMiddleoption);
		
	}
});

	
//不同状态统计
var myChartContentRight = echarts.init(document.getElementById('content-right'));
var myChartContentRightoption = {    
    title : {
        text: '不同状态统计',
        x:'left'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{b} : {c} ({d}%)"
    },
    legend: {
        left: 'center',
        top: '15%',
        data: ['run','pause','error']
    },
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:status1, name:'run'},
                {value:status2, name:'pause'},
                {value:status3, name:'error'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
myChartContentRight.setOption(myChartContentRightoption);