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

// function get_dp_reviewNum() {
//     n = 2643376
//     $.ajax({
//         url: schema_url + '/get_dp_reviewNum',
//         type: 'GET',
//         data:{"id" : n},
//         dataTpye: "json",
//         success: function (res) {
//             console.log(res)
//         },
//         error: function (XMLHttpRequest, textStatus, errorThrown) {
//             console.log(XMLHttpRequest.status);
//             console.log(XMLHttpRequest.readyState);
//             console.log(textStatus);
//         }
//     })
// }
//
// function get_ta_reviewNum() {
//     n = 5292664
//     $.ajax({
//         url: schema_url + '/get_ta_reviewNum',
//         type: 'GET',
//         data:{"id" : n},
//         dataTpye: "json",
//         success: function (res) {
//             console.log(res)
//         },
//         error: function (XMLHttpRequest, textStatus, errorThrown) {
//             console.log(XMLHttpRequest.status);
//             console.log(XMLHttpRequest.readyState);
//             console.log(textStatus);
//         }
//     })
// }
//
// function get_or_reviewNum() {
//     n = 5247
//     $.ajax({
//         url: schema_url + '/get_or_reviewNum',
//         type: 'GET',
//         data:{"id" : n},
//         dataTpye: "json",
//         success: function (res) {
//             console.log(res)
//         },
//         error: function (XMLHttpRequest, textStatus, errorThrown) {
//             console.log(XMLHttpRequest.status);
//             console.log(XMLHttpRequest.readyState);
//             console.log(textStatus);
//         }
//     })
// }
//
// function get_mfw_reviewNum() {
//     n = 11745626
//     $.ajax({
//         url: schema_url + '/get_mfw_reviewNum',
//         type: 'GET',
//         data:{"id" : n},
//         dataTpye: "json",
//         success: function (res) {
//             console.log(res)
//         },
//         error: function (XMLHttpRequest, textStatus, errorThrown) {
//             console.log(XMLHttpRequest.status);
//             console.log(XMLHttpRequest.readyState);
//             console.log(textStatus);
//         }
//     })
// }
function get_all_id() {
    n = 4
    $.ajax({
        url: schema_url + '/get_all_id',
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