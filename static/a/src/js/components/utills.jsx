
export function makeAjaxCall(_url, _data){

    var returnContent = '';

    $.ajax({
        url: _url,
        method: 'POST',
        data: _data,
        cache: false,
        async: false,
        success: function(_response){
            returnContent = _response;
        }
    });

    return returnContent;


}