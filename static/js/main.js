$(document).ready(function() {
    $("#page").children().children().mouseover(function(){
        if($(this).attr("id")=='pageId'){
            $(this).css("cursor","auto");
            $(this).css("border","1px solid #0099ff");
            $(this).children().css("color","#0099ff");
        }else{
            $(this).css({"background-color":'#0099ff',"text-decoration":"none","cursor":"pointer"});
            $(this).children().css("color","#f8f8f8");
        }
    });
    $("#page").children().children().mouseleave(function(){
        if($(this).attr("id")=='pageId'){
            $(this).css("cursor","auto");
            $(this).css("border","1px solid #0099ff");
            $(this).children().css("color","#0099ff");
        }else{
            $(this).css({"background-color":'#F8F8F8',"text-decoration":"none","cursor":"pointer"});
            $(this).children().css("color","#333");
        }
    
    });
});

