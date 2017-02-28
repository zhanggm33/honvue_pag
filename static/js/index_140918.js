$(function(){
	var $index_Banner = $("#index_Banner"),
		$ban_Ovh = $("#ban_Ovh"),
		$ban_Nav = $("#ban_Nav"),
		$ban_Ovh_List = $ban_Ovh.find(".banCon"),
		$ban_Ovh_Lnum = $ban_Ovh_List.length,
		$sTime = 6000,
		$ban_N = 1,
		$ban_time=null,
		$ban_noclick=false;
	(function(){
		var $s = 0,
			$html = "";
		for(;$s < $ban_Ovh_Lnum;$s++){
			$html += $s == 0 ? "<em class=\"on\"></em>" : "<em></em>";
			}
		$ban_Nav.html($html).css({"opacity":1,"top":(350-22*$ban_Ovh_Lnum)/2});
		$ban_Ovh_List.eq(0).css({"display":"block","opacity":1}).addClass("on").siblings().css({"display":"block","opacity":0});;
		$ban_Nav.addClass("banNc01");
		}());
	function fnFocusAct(n){
		clearInterval($ban_time);
		$ban_Ovh.find(".on").stop().fadeTo(400,0,function(){
			$(this).removeClass("on");
			});
		$ban_Ovh_List.eq(n).addClass("on").stop().fadeTo(400,1,function(){
			$ban_N == $ban_Ovh_Lnum-1 ? $ban_N=0 : $ban_N++;
			if(!$ban_noclick) $ban_time = setTimeout(ban_Fun,$sTime);
			});
		$ban_Nav.attr('class',"pa zi03 ban_Nav banNc0"+(n+1)).find("em").eq(n).addClass("on").siblings(".on").removeClass("on");		
		}
	function ban_Fun(){
		fnFocusAct($ban_N);
		}
	$ban_time = setTimeout(ban_Fun,$sTime);
	$index_Banner.hover(function(){
		$ban_noclick=true;
		clearInterval($ban_time);
		},function(){
			$ban_noclick=false;
			$ban_time = setTimeout(ban_Fun,$sTime);
		})
	$ban_Nav.on("click","em",function(){
		var $this = $(this);
			$ban_N = $this.index();
		if($this.hasClass("on")){
			return false;
			}else{
				clearInterval($ban_time);
				fnFocusAct($ban_N);	
				}
		//alert($eIndex);
		});
	$ban_Ovh_List.click(function(){
		var $this = $(this),
			$tUrl = $this.attr("data-href");
		if($tUrl == "") return;
		window.open($tUrl);		
		});
});