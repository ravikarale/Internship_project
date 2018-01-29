function getSelected(){
	var chkArray = [];
	$(".chk:checked").each(function() {
		chkArray.push($(this).val());
	});
	
	var selected;
	selected = chkArray.join(',') + ",";

	if(selected.length > 1){
		alert("You have selected " + selected);	

		$.ajax({
	 	type: "POST",
        url: "/sendTo",
        data: chkArray,
        dataType: "html",
        success: function (data) {
            alert("Successfully sent the URL to Django");
          },
        error: function(){
                alert("error");
            },
      });
	}else{
		alert("Please at least one of the checkbox");	
	}


	 
}





