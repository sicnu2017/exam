/**
 * Created by Wang on 2017/11/27.
 */
/*-----------------------------setExam----------------------------------*/
// $(document).on("click", "{% url 'addNewExam' %}",function(e){
//     e=window.event || e;
//     e.preventDefault();
//     var href=$(this).attr("href");
//     var url=""+href;
//     $.get(url).done(function(response){
//         $("#content").html(response);
//     });
// });
$(document).on("click","#makePaper",function(e){
    e=window.event || e;
    e.preventDefault();
    $.get("makePaper.html").done(function(response){
        $("#content").html(response);
    });
})
/*-----------------------------addNewExam-----------------------------------------*/
$(document).on("focus","#examTime",function(e){
    $( "#examTime" ).datepicker({
        altField: "#actualDate",
        buttonImageOnly: true,
        dateFormat: "yy-mm-dd"
    });
});
$(document).on("click",".majorOpt",function(e){
    var e=window.event||ev;
    var option=e.target||e.srcElement;
   // var selectVal=$(this).val();
    //console.log($(this).val());
    console.log("option"+$(option).html());
    //$("#majorSelect").remove($(option));
    //$(this).val(selectVal+$(this).val);

    /*$( ".selector" ).selectmenu({
        select: function( event, ui ) {
            console.log($(this).val());
        }
    });*/
})
var layer;
layui.use('layer', function(){
    layer = layui.layer;
});
//提交考试申请
$(document).on("click","#commitBtn",function(){
    layer.open({
        title: '系统提示',
        content: '已提交，等待管理员审核',
        icon:6,
        yes: function(index, layero){
            $.get("setExam.html").done(function(response){
                $("#content").html(response);
                layer.close(index);   //如果设定了yes回调，需进行手工关闭
            });
        }
    });
});
//点击取消考试申请
$(document).on("click","#cancelBtn",function(){
    layer.open({
        title: '系统提示',
        content: '确认放弃？',
        icon:3,
        yes: function(index, layero){
            $.get("setExam.html").done(function(response){
                $("#content").html(response);
                layer.close(index);   //如果设定了yes回调，需进行手工关闭
            });
        }
    });
})

/*----------------------makePaper----------------------------*/
var defaultSelections=$("#selectionsContainer").html();
$(document).on("change","#quesType",function(){
    var quesType=$(this).val();
    switch (quesType){
        case "选择题":
            console.log("----------");
            $("#judgeDiv").css({display:"none"});
            $("#selectionDiv").css({display:"block"});
            break;
        case "填空题":
            $("#selectionDiv").css({display:"none"});
            $("#judgeDiv").css({display:"none"});
            break;
        case "判断题":
            $("#selectionDiv").css({display:"none"});
            $("#judgeDiv").css({display:"block"});
            break;
        case "简答题":
            $("#selectionDiv").css({display:"none"});
            $("#judgeDiv").css({display:"none"});
            break;
        case "程序设计题":
            $("#selectionDiv").css({display:"none"});
            $("#judgeDiv").css({display:"none"});
            break;
    }
});
var selects=['A','B','C','D','E','F','G','H','I','J'];
$(document).on("change","#selectNum",function(){
    var num=$(this).val();
    var selectContent="";
    for(var i=0;i<num;i++) {
        var select = "<div class='container-div'>" +
                         "<div class='form-group'>" +
                            "<div class='input-group'>" +
                                "<span class='input-group-addon bg-primary'>" +
                                    "<label class='radio-inline'>" +
                                        "<input type='radio' name='singleSelectRadio' id=''"+selects[i].toLowerCase()+"Radio'> " + selects[i] +
                                    "</label>" +
                                    "</span>" +
                                    "<input type='text' class='form-control' placeholder='请输入选项内容'>" +
                            "</div>" +
                        "</div>" +
                     "</div>";
        selectContent+=select;
    }
    $(".selectionsContainer").html(selectContent);
})
