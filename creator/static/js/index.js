function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
						var cookie = jQuery.trim(cookies[i]);
						// Does this cookie string begin with the name we want?
						if (cookie.substring(0, name.length + 1) === (name + '=')) {
								cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
								break;
						}
				}
		}
		return cookieValue;
}

 function SaveData(user_id){
	var pre_id = "present"+user_id;
	var paid_id = "paid"+user_id;
	paid = (document.getElementById(paid_id).checked ? 1 : 0);
	present = (document.getElementById(pre_id).checked ? 1 : 0);
	// console.log("paid: " + paid);
	// console.log("present: " + present);
	data = {
		"id": form_id,
		"paid": paid,
		"present": present 
	};
	makeCall(data,"/register/save/");
};

function makeCall(data,url){
	// validation for Cross Site Request Forgery protection
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	});
	// make call
	$.ajax({
			type: "POST",
			url: url,
			data: data,
			error: function(xhr, ajaxOptions, err){
				$.notify(err,'error');
			}.bind(this)

		}).done(function(data){
			$.notify.defaults({autoHideDelay: 1000}); 
			//console.log(log);
			$.notify(data,'success')
		});
}