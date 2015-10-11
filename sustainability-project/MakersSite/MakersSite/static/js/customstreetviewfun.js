var panorama;
      var geocoder;
      function initPano() {
      geocoder = new google.maps.Geocoder();
      panorama = new google.maps.StreetViewPanorama(
      document.getElementById('pano'), {
      position: {lat: 37.869, lng: -122.255},
      pov: {
      heading: 270,
      pitch: 0
      },
      visible: true,
      linksControl: false,
      panControl: false,
      enableCloseButton: false
      });

      panorama.addListener('pano_changed', function() {
      var panoCell = document.getElementById('pano-cell');
      panoCell.innerHTML = panorama.getPano();
      });

      panorama.addListener('links_changed', function() {
      var linksTable = document.getElementById('links_table');
      while (linksTable.hasChildNodes()) {
      linksTable.removeChild(linksTable.lastChild);
      }
      var links = panorama.getLinks();
      for (var i in links) {
      var row = document.createElement('tr');
      linksTable.appendChild(row);
      var labelCell = document.createElement('td');
      labelCell.innerHTML = '<b>Link: ' + i + '</b>';
      var valueCell = document.createElement('td');
      valueCell.innerHTML = links[i].description;
      linksTable.appendChild(labelCell);
      linksTable.appendChild(valueCell);
      }
      });

      /*    panorama.addListener('thing', function(){
      //panorama.setPosition(panorama.getPosition());
      alert(panorama.getPosition());
      });
      */
      
      panorama.addListener('position_changed', function() {
      var positionCell = document.getElementById('position-cell');
      positionCell.firstChild.nodeValue = panorama.getPosition() + '';
      });

      panorama.addListener('pov_changed', function() {
      var headingCell = document.getElementById('heading-cell');
      var pitchCell = document.getElementById('pitch-cell');
      headingCell.firstChild.nodeValue = panorama.getPov().heading + '';
      pitchCell.firstChild.nodeValue = panorama.getPov().pitch + '';
      });
      }
      

function forward(parameter){
      //        alert(panorama.getPosition().lat());
      //          alert(panorama.getPosition().lat()+5.0);
      //        var angle =45;
      
      //alert(Object.keys(panorama.getLinks()[0]));
      panorama.setPosition({lat: panorama.getPosition().lat()-0.0002*Math.sin(panorama.getPov().heading) ,
      lng: panorama.getPosition().lng()-0.0002*Math.cos(panorama.getPov().heading)} );
      
      /*panorama.setPosition({lat: panorama.getPosition().lat()-0.0002*Math.sin(parseFloat(parameter)) ,
      lng: panorama.getPosition().lng()-0.0002*Math.cos(parseFloat(paramter))} );
      */
      }
      
      function backward(parameter){

      panorama.setPosition({lat: panorama.getPosition().lat()+0.0002*Math.sin(panorama.getPov().heading),
      lng: panorama.getPosition().lng()+0.0002*Math.cos(panorama.getPov().heading)} );
/*
      panorama.setPosition({lat: panorama.getPosition().lat()+0.0002*Math.sin(parseFloat(parameter)) ,
      lng: panorama.getPosition().lng()+0.0002*Math.cos(parseFloat(paramter))} );
  */   
      }
      function povmanip(){
      //alert( panorama.getPov().heading);
      panorama.setPov({
      heading: panorama.getPov().heading+10,
      pitch: panorama.getPov().pitch,
      })
      }
        function left(){
      //currentheading+=15;
      panorama.setPov({
      heading: (panorama.getPov().heading+15),
      pitch: panorama.getPov().pitch,
      });
      }
      function right(){
      //currentheading-=15;
      panorama.setPov({
      heading: (panorama.getPov().heading-15),
      pitch: panorama.getPov().pitch,
      });
      }
      function up(){    
      panorama.setPov({
      heading: panorama.getPov().heading,
      pitch: panorama.getPov().pitch+15,
      });
      }
      function down(){    
      panorama.setPov({
      heading: panorama.getPov().heading,
      pitch: panorama.getPov().pitch-15,
      });
      }
      //http://stackoverflow.com/questions/6882965/google-maps-api-v3-get-map-by-address
      function codeAddress() {
          var address = document.getElementById('address').value;
      if (address.search(/-?[0-9]+\.[0-9]+\ *,\ *-?[0-9]+\.[0-9]+/i) == -1){
         geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
      //panorama.setCenter(results[0].geometry.location);
      //alert(results[0].geometry.location.lat() +" "+results[0].geometry.location.lng());
      panorama.setPosition({lat: results[0].geometry.location.lat(),
      lng: results[0].geometry.location.lng()} );
      }
      else {
      alert('Geocode was not successful for the following reason: ' + status);
      }
      
      });
      }
      else{
      //I'm sorry for the lisp type stuff
      var lat=float(address.split(",")[0]);
      var lng=float(address.split(",")[1]);
      panorama.setPosition({lat: lat, lng: lng} );
      }
      }
      //48.8588871 2.294486099999972 //Eiffel Tower
      //35.138927, -90.045577 // Beale Street Memphis
      //38.89767579999999 -77.03648269999997 //White House
      //36.1486927 -86.8037597 // Vandy
