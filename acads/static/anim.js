$( "#title" ).delay(2000).slideUp( "slow",function()
{$("#dept").slideDown("slow");
});
$(".click").click(function(){
  $("#dept").slideUp("slow",function(){
    $("#year").slideDown("slow");
  });
});
$("#no").click(function(){               //convert .click to .submit during AJAXifyy
  $("#register").slideUp("slow",function(){
    $("#name_form").slideDown("slow");
  });
});
