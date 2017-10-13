$('section .option li').eq(1).addClass('active');
	
var timeArr = ["2017-1","2017-2","2017-3","2017-4","2014-5","2017-6","2017-7"];
var runArr = [0,0,0,0,0,0,0];
var errorArr = [0,0,0,0,0,0,0];
var pauseArr = [0,0,0,0,0,0,0];
$.ajax({
	url:url_head +"get_spider_num_group_by_month",
	type:"get",
	data: {"date":"2017"},
	dateType:"json",
	success:function(result){
		console.log(result);
		for(i=0;i<result[0].run.length;i++){
			var timeObj1 = result[0].run[i].m;
			var timeObj = "2017-" + timeObj1;
			timeArr.push(timeObj);
			var runObj = result[0].run[i].n;
			runArr.push(runObj);
		}
		for(i=0;i<result[1].error.length;i++){
			var errorObj = result[1].error[i].n;
			errorArr.push(errorObj);
		}
		for(i=0;i<result[2].pause.length;i++){
			var pauseObj = result[2].pause[i].n;
			pauseArr.push(pauseObj);
		}
		console.log(timeArr);
		console.log(runArr);
		console.log(errorArr);
		console.log(pauseArr);
		
		var myChartTwo = echarts.init(document.getElementById('MonthRun'));
		var myChartTwooption = {
		    title : {
//				    text: '某地区蒸发量和降水量',
//				    subtext: '纯属虚构'
		    },
		    tooltip : {
		        trigger: 'axis'
		    },
		    legend: {
		        data:['run', 'pause', 'error']
		    },
		    toolbox: {
		        show : true,
		        feature : {
		            dataView : {show: true, readOnly: false},
		            magicType : {show: true, type: ['line', 'bar']},
		            restore : {show: true},
		            saveAsImage : {show: true}
		        }
		    },
		    calculable : true,
		    xAxis : [
		        {
		            type : 'category',
		            data : timeArr
		        }
		    ],
		    yAxis : [
		        {
		            type : 'value'
		        }
		    ],
		    series : [
		        {
		            name:'run',
		            type:'bar',
		            data:runArr,
		            markPoint : {
		                data : [
		                    {type : 'max', name: '最大值'},
		                    {type : 'min', name: '最小值'}
		                ]
		            }
		        },
		        {
		            name:'pause',
		            type:'bar',
		            data:pauseArr,
		            markPoint : {
		                data : [
		                    {type : 'max', name: '最大值'},
		                    {type : 'min', name: '最小值'}
		                ]
		            }
		        },
		        {
		            name:'error',
		            type:'bar',
		            data:errorArr,
		            markPoint : {
		                data : [
		                    {type : 'max', name: '最大值'},
		                    {type : 'min', name: '最小值'}
		                ]
		            }
		        }
		    ]
		};
		myChartTwo.setOption(myChartTwooption);
		
	}
});