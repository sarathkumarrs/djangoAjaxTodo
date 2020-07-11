$(document).ready(function(){
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    $('#createbutton').click(function(){
        var serialisedData = $('#createtaskform').serialize();
        $.ajax({
            url : $('#createtaskform').data('url'),
            data : serialisedData,
            type : 'POST',
            success: function(response){
                $('#tasklist').append('<div class="card mb-1" id="taskcard" data-id="'+response.task.id+'"><div class="card-body">'+response.task.title+'<button type="button" class="close float-right" data-id="'+response.task.id+'"><span>&times;</span></button></div></div>')
            }
        })
        $('#createtaskform')[0].reset();
    });
    $('#tasklist').on('click', '.card',function(){
        var dataId = $(this).data('id');
        console.log(dataId)

        $.ajax({
            url: '/tasks/' + dataId + '/compleated/',
            data : {
                csrfmiddlewaretoken: csrfToken,
                id : dataId
            },
            type : 'POST',
            success : function(){
                var cardItem = $('#taskcard[data-id="'+dataId +'"]');
                cardItem.css('text-decoration','line-through').hide().slideDown();
                $('#tasklist').append(cardItem);
            }
        })
    }).on('click','button.close',function(event){
        event.stopPropagation();

        var dataId = $(this).data('id');

        $.ajax({
            url: '/tasks/' + dataId + '/delete/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id : dataId
            },
            type: 'POST',
            datatype: 'json',
            success: function(){
                $('#taskcard[data-id="'+ dataId +'"').remove();
            }
        })
    });
});