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

        var modal = $('#modal');
        var container = modal.find('.modal-container');
        container.empty();

        modal.find('.modal-title').text(button.attr('title'));

        container.load(url + ' form', function (e) {
            var action = container.find('form').attr('action');

            // refresh select picker widget.
            container.find('.selectpicker').selectpicker('refresh');

            // refresh autogrow.
            container.find('textarea').css('min-height', '72px');
            container.find('textarea').autogrow({vertical: true, horizontal: false, flickering: false});

            // set action if form used blank as action url.
            if (action == "") {
                container.find('form').attr('action', url);
            }
        });

        modal.modal('show');
    });
});
