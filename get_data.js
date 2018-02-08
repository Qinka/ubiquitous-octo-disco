var urls = [];

function my_get_data(currentPage,qtext,sort,type,vtime,datepid,channel,pageNum,pageflag){
    var cp = eval(currentPage);
	  var video_html ="";
    var findnum ="";
    var ref="";
    $('.search17354_ind03 .ind03 .jieguo .outer .timg').css('display','block');
	  $.ajax({
	      url:"ifsearch.php",
	      type:"get",
	      async:false,
	      dataType:"json",
	      data:{page:currentPage,qtext:qtext,sort:sort,pageSize:pageNum,type:type,vtime:vtime,datepid:datepid,channel:channel,pageflag:pageflag},
	      success:function(re) {
	    	    if (re.totalpage >= cp){
                for(i = 0; i < re.list.length;++i){
                    urls.push(re.list[i].urllink);
                    console.log(re.list[i].urllink);
                }
                my_get_data(cp+1+"",qtext,sort,type,vtime,datepid,channel,pageNum,pageflag);
            }
        }
    }
          );
}


var text = "";
for (i=0; i < urls.length;i++)
    text += urls[i] + "\n";
