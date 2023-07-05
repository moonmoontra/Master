$(document).ready(function() {
    if ($('body').hasClass('dark-theme')) {
        $('#setting-collapse li:nth-child(2)').hide();
        $('#setting-collapse li:nth-child(3)').show();
    } else {
        $('#setting-collapse li:nth-child(3)').hide();
        $('#setting-collapse li:nth-child(2)').show();
    }
});