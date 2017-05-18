$( "#title" ).delay(2000).slideUp( "slow",function()
{$("#dept").slideDown("slow");
});
$(".click").click(function(){
  $("#dept").slideUp("slow",function(){
    $("#year").slideDown("slow");
  });
});
