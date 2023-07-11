jQuery(document).ready(function($) {
    $('.to').click((e) => {
    $(e.target).find(".toh").toggleClass("on").toggleClass("off");
    });
});
