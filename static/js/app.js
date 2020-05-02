$("document").ready(function(){
    $("#send").click(function(){
        var message = $("#message").val();
        $.ajax({
            url: "https://grandpytest.herokuapp.com/api/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"message": message})
        }).done(function(data) {
            var inside = "<div class=\"spinner-border text-primary\" role=\"status\"> <span class=\"sr-only\">Loading...</span></div>"
            document.getElementById("coordinates").innerHTML = inside;
            document.getElementById("map").innerHTML = " ";
            document.getElementById("wikitext").innerHTML = " ";
        }).done(function(data) {
            var myCity = data[0]['myCity']
            var myText = data[2]['myText']
            var myTitle = data[3]['myTitle']
            console.log(myTitle)
            setTimeout(function(){ 
                document.getElementById("wikitext").innerHTML = "<p>" + myText +"</p> <a href=\""+myTitle+"\">Lien Wikipedia</a>"; }, 1000);
        }).done(function(data) {
            var myCity = data[0]['myCity']
            var myList = data[1]['myList']
            setTimeout(function(){ 
                document.getElementById("coordinates").innerHTML = "<p class=\"text-justify\">" + myCity + " se trouve aux coordonnées " + myList + ".</p>"; }, 1000);
        }).done(function(data) {
            var myList = data[1]['myList']
            var uluru = {lat: myList[0], lng: myList[1]};
            setTimeout(function(){ 
                var map = new google.maps.Map(
                    document.getElementById('map'), {zoom: 11, center: uluru});
                var marker = new google.maps.Marker({position: uluru, map: map});
            }, 1000);
        });
    });
});