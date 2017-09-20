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



function get_or_memberNum() {
    n = 5247
    $.ajax({
        url: schema_url + '/get_or_memberNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_dp_memberNum() {
    n = 2643376
    $.ajax({
        url: schema_url + '/get_dp_memberNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_ta_memberNum() {
    n = 5292664
    $.ajax({
        url: schema_url + '/get_ta_memberNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_mfw_memberNum() {
    n = 669
    $.ajax({
        url: schema_url + '/get_mfw_memberNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_dp_womemNum() {
    n = 2643376
    $.ajax({
        url: schema_url + '/get_dp_womemNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_dp_memNum() {
    n = 2643376
    $.ajax({
        url: schema_url + '/get_dp_memNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_mfw_memNum() {
    n = 669
    $.ajax({
        url: schema_url + '/get_mfw_memNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_mfw_womemNum() {
    n = 669
    $.ajax({
        url: schema_url + '/get_mfw_womemNum',
        type: 'GET',
        data:{"id" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_or_favorite() {
    n = 1
    $.ajax({
        url: schema_url + '/get_or_favorite',
        type: 'GET',
        data:{"star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_or_location() {
    n = 1
    $.ajax({
        url: schema_url + '/get_or_location',
        type: 'GET',
        data:{"star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_dp_location() {
    n = 1
    $.ajax({
        url: schema_url + '/get_dp_location',
        type: 'GET',
        data:{"star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_ta_location() {
    n = 1
    $.ajax({
        url: schema_url + '/get_ta_location',
        type: 'GET',
        data:{"star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}

function get_mfw_location() {
    n = 1
    $.ajax({
        url: schema_url + '/get_mfw_location',
        type: 'GET',
        data:{"star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}