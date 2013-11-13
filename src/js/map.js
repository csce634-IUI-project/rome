goog.provide('hs.map');

hs.map = function (latitude, longitude) {
  mapOptions = {
    center: new google.maps.LatLng(latitude, longitude),
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById('map'), mapOptions);
}
