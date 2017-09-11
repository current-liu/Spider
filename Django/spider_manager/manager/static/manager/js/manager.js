/**
 * Created by Administrator on 2017/9/1 0001.
 */
function fun(){
    var id = 1
    $.ajax({
        url:schema_url+'/ajax',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}
function get_projects(){
    $.ajax({
        url:schema_url+'/get_projects',
        type:'GET',
        data:{"id":1},
        dataTpye:"jsonp",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_spiders_in_project(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_spiders_in_project',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_project(){
    $.ajax({
        url:schema_url+'/get_project',
        type:'GET',
        data:{"id":1},
        dataTpye:"jsonp",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_spider(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_spider',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spiders(){

    $.ajax({
        url:schema_url+'/get_spiders',
        type:'GET',

        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spiderstatus(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_spiderstatus',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spiderstatus_today(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_spiderstatus_today',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spiderstatus_last(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_spiderstatus_last',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}


function get_spider_group_on_status(){
    n = 1
    $.ajax({
        url:schema_url+'/get_spider_group_by_status',
        type:'GET',
        data:{"status" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spider_on_date() {
    n = "2017-09-07"
    $.ajax({
        url:schema_url+'/get_spider_on_date',
        type:'GET',
        data:{"date" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_error_spider_on_date() {
    n = "2017-09-07"
    $.ajax({
        url:schema_url+'/get_error_spider_on_date',
        type:'GET',
        data:{"date" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spider_on_month() {
    n = "2017-09"
    $.ajax({
        url:schema_url+'/get_spider_on_date',
        type:'GET',
        data:{"date" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_error_spider_on_month() {
    n = "2017-09"
    $.ajax({
        url:schema_url+'/get_error_spider_on_date',
        type:'GET',
        data:{"date" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}


function get_spider_on_month_every_day() {
    n = "2017-09"
    $.ajax({
        url:schema_url+'/get_spider_on_month_every_day',
        type:'GET',
        data:{"date" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}


function get_spider_on_year_every_month() {
    n = "2017"
    $.ajax({
        url:schema_url+'/get_spider_on_year_every_month',
        type:'GET',
        data:{"date" : n, "status": 3},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_spider_on_day_every_hour() {
    n = "2017-09-06"
    $.ajax({
        url:schema_url+'/get_spider_on_day_every_hour',
        type:'GET',
        data:{"date" : n},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}

function get_operation_time_last_n_days() {
    n = 5
    n_days = 7
    $.ajax({
        url:schema_url+'/get_operation_time_last_n_days',
        type:'GET',
        data:{"id" : n, "n": n_days},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }

    })
}