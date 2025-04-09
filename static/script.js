$(document).ready(function() {
    $("#startProcess").click(function() {
        $("#spinner").show();
        $("#result").text("");

        $.get("/process", function(data) {
            $("#spinner").hide();
            $("#result").text(data.message);
        });
    });
    $("#secondProcess").click(function() {
        $("#spinner2").show();
        $("#display").text("");

        $.get("/secondProcess", function(data) {
            $("#spinner2").hide();
            $("#display").text(data.value);
        });
    });
});