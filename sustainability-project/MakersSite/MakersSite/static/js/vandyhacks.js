      function forward(){
      panorama.setPosition({lat: panorama.getPosition().lat()+0.0002*Math.sin(panorama.getPov().heading) ,
      lng: panorama.getPosition().lng()+0.0002*Math.cos(panorama.getPov().heading)} );
//      console.log("function called");
      }
      function backward(){
      panorama.setPosition({lat: panorama.getPosition().lat()-0.0002*Math.sin(panorama.getPov().heading),
      lng: panorama.getPosition().lng()-0.0002*Math.cos(panorama.getPov().heading)} );
      }
      function left(){
    
      panorama.setPov({
      heading: (panorama.getPov().heading+15)% 180,
      pitch: panorama.getPov().pitch,
      })
      }
      function right(){
    
      panorama.setPov({
      heading: (panorama.getPov().heading-15)%180,
      pitch: panorama.getPov().pitch,
      })
      }
