

getSelectedRow = function(val)
    {
        db.transaction(function(transaction) {
              transaction.executeSql('SELECT * FROM Employ where number = parseInt(val);',[], selectedRowValues, errorHandler);

        });
    };
    selectedRowValues = function(transaction,results)
    {
         for(var i = 0; i < results.rows.length; i++)
         {
             var row = results.rows.item(i);
             alert(row['number']);
             alert(row['name']);                 
         }
    };




function getLogin()
{
	console.log(document.getElementById('login-name').value);
	console.log(document.getElementById('login-pass').value);

	var uName = document.getElementById('login-name').value;
	var uPass = document.getElementById('login-pass').value;
	

	loginForm = '{'+'"title":"'+uName+'","text"' + ':"'+ uPass +'"}';

	$.ajax({
		type:'POST';
		url: 'http://127.0.0.1:8000/pcm_home',
		type: 'default GET (Other values: POST)',
		dataType: json,
		data:{
			nam
		}
	})
	.done(function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	



	// var xhttp = new XMLHttpRequest();
 //    xhttp.onreadystatechange = function() {
 //            if (this.readyState == 4 && this.status == 200)
 //            {
 //        var res = this.responseText;
 //        if(res == 0)
 //        {
 //            var msg = "Invalid Username and Password";
 //                        document.getElementById("result").innerHTML = msg;
 //            alert("Invalid Username and Password");
 //                        document.getElementById("userUsername").value = "";
 //                        document.getElementById("userPassword").value = "";
 //        }
 //        else if(res == 1)
 //        {
 //            var msg = "You are Logged In...";
 //                        document.getElementById("result").innerHTML = msg;
 //            alert("You are Logged In...");
 //                        document.getElementById("userUsername").value = "";
 //                        document.getElementById("userPassword").value = "";
 //            window.location.href="./afterLogin.html";
 //        }
 //            }
 //    };
 //    xhttp.open("POST", "./userLogin.py/userLogin", true);
 //    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
 //    xhttp.send("FormData="+uUsername+" "+uPassword);

}