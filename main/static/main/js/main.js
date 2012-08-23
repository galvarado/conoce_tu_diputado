// State IDS
var states = [
  'AGU','BCN','BCS','CAM','CHH',
  'CHP','COA','COL','DIF','DUR',
  'GRO','GUA','HID','JAL','MEX',
  'MIC','MOR','NAY','NLE','OAX',
  'PUE','QUE','ROO','SIN','SLP',
  'SON','TAB','TAM','TLA','VER',
  'YUC','ZAC'
];
// State Names
var state_names = [
  'Aguascalientes', 'Baja California Norte', 'Baja California Sur', 'Campeche',
  'Chihuahua','Chiapas','Coahuila','Colima','Distrito Federal','Durango','Guerrero',
  'Guanajuato','Hidalgo','Jalisco','Edo. Mexico','Michoacán','Morelos','Nayarit',
  'Nuevo León','Oaxaca','Puebla','Queretaro','Quintana Roo','Sinaloa','San Luis Potosí',
  'Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz','Yucatán','Zacatecas'
];
$(function() {
  // Activate map highlight funcionality
  $('#map').maphilight();
  // When user is over an state
  $('.area').hover(function() {
    // Obtain name of state dependind his id and put it in the info div
    var id= $(this).attr('id');
    var state = $.inArray(id,states);
    $('#info').html(state_names[state]);
  }, function(){
    // Erase info div when user leave an state
    $('#info').html('');
  });
});