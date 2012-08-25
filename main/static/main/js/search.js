$(function() {
  // Initialize table
  datatable = $('#deputies-search-datatable').dataTable({
    "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
    "sPaginationType": "bootstrap",
    "bProcessing": true,
    "sAjaxSource": "search/get_deputies",
    "bServerSide": true,
    "oLanguage": {
      "sUrl": STATIC_URL + "main/js/libs/dataTables.spanish.txt"
    },
    "aoColumns": [
        { "sWidth": "25%" },
        { "sWidth": "25%" },
        { "sWidth": "15%" },
        { "sWidth": "15%" },
        { "sWidth": "15%" },
        { "sWidth": "15%" },
    ],
    // Fill the table with ajax source
    "fnServerData": function ( sSource, aoData, fnCallback ) {
      $.ajax({
        "dataType": 'json',
        "type": "POST",
        "url": sSource,
        "data": aoData,
        "success": fnCallback
      });
    }
  });
  $('#specific-search').keyup(function(){
    datatable.fnFilter($(this).val());
  });
  $('.image-to-search').live('click', function() {
    $('input').val('');
    datatable.fnFilter($(this).attr('alt'));
  });
});