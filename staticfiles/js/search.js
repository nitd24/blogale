function displayResults(data){
    var html = '';
    var searchResults = data.hits;
    var dataLength = data.total;
    for(i=0;i<dataLength;i++){
        var shortDescription = jQuery.trim(searchResults[i]._source.description).substring(0, 450)
                            .split(" ").slice(0, -1).join(" ") + "...";
        html += '<hr>' +
            '<div class="row">' +
            '    <div class="col-md-1"><span class="glyphicon glyphicon-hand-right"></span></div>' +
             '   <div class="col-md-11">' +
             '       <h4 style="margin-top:0px"><a href="/blog/' + searchResults[i]._id + '">' + searchResults[i]._source.title + '</a></h4>' +
            '      <p>' + shortDescription + '</p>' +
             '       <p><a href="/blog/' + searchResults[i]._id + '">Read more...</a></p>' +
            '    </div>' +
            '</div>';
    }

    $('#searchResults').html(html);
}


function getSearchResults(){
    //console.log('search initiated with search term :: ' + $('#searchBox').val());

     var query = $('#searchBox').val();
     if (query.length == 0){
        $('.well').show();
         $('#searchQuery').html('Please enter a search term.');
        return false;
     }
    $('#searchQuery').html('Showing results for : <strong>' +query + '</strong>');
    var data = {
                query:{match:{_all:query}}
            }

      $.ajax({
        url: 'http://localhost:9200/blog/_search',
        type: 'POST',
        crossDomain : true,
        data: JSON.stringify(data),
        success: function(res) {
            $('.well').show();
            if(res.hits.total > 0){
                 $('#searchQuery').append(' | got ' + res.hits.total + ' results in ' + (res.took * 0.001) + ' seconds.');
                displayResults(res.hits);
            }else{
                $('#searchResults').html("No results found.");
            }
        },
        error : function(e){
            console.log("ERROR ::: " + JSON.stringify(e));
        }
    });
}


$(function(){
    $('#searchBtn').click(getSearchResults);
});
