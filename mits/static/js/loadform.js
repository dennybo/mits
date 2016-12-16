$(function () {
    /*
     * Loads a form into a modal, the modal should be identified as #modal, and the object clicked
     * must have the "load-modal" class, and the attributes: "href" and "title", where title is displayed
     * in the modal title.
     */
    $('.load-modal').click(function (e) {
        e.preventDefault();

        var button = $(this);
        var url = button.attr('href');

        console.log(button);

        var modal = $('#modal');
        var container = modal.find('.modal-container');

        modal.find('.modal-title').text(button.attr('title'));

        container.load(url + ' form', function (e) {
            var action = container.find('form').attr('action');

            if (action == "") {
                container.find('form').attr('action', url);
            }
        });

        modal.modal('show');
    });
});
