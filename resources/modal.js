$(document).ready(function() {
    $("#content").load("home.html");

    $(".annoModal").click(function() {
        var page = $(this).attr("href");
        $(".modal-body").load(page);
        return false;
        });
})