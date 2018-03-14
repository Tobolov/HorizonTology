function change_font_size(difference) {
    var div = $("#result")
    var fontSize = parseInt(div.css("font-size"));
    fontSize = fontSize + difference;
    div.css({'font-size':fontSize + "px"});

    $("#font-current").attr("data-text", fontSize);
}

$('#font-increase').click(function() {
   change_font_size(1)
});

$('#font-decrease').click(function() {
   change_font_size(-1)
});

$('#try-again').click(function() {
   window.location.href = "app.html";
});

$('#share').click(function() {
   $('#to-implement').modal('show');
});

$('#copy-text').popup();
$('#font-increase').popup();
$('#font-decrease').popup();