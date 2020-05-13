$(document).ready(function() {
    $('#search-btn').on('click',  function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/consoles?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well console">
                                <a href="/consoles/${d.id}">
                                    <img class="console-img" src="${d.firstImage}"/>
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>`
                });
                $('.consoles').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, statur, error) {
                // TODO: Show toastr
                console.error(error);
            }


        })
    });
});