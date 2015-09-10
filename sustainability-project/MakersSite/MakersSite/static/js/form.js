
//Stephen Kinser

/*
I hate global variables my bad
*/
var state=0;
var listOfArrays;
function matrix(matnum){
    //alert("here");
        //var x =  document.getElementById("inputform");
        var createform = document.createElement('form');
        //createform.setAttribute("action","");
        //createform.setAttribute("method","post");
        //x.appendChild(createform);

            var colsize=document.getElementById(matnum.toString()+"y").value;
            var rowsize=document.getElementById(matnum.toString()+"x").value;
            //alert(colsize.toString() +" "+ rowsize.toString())
            text="<form>";
            for(i=1; i <= rowsize ; i++){
                for(j=1; j <= colsize; j++){

                    text+= "Array "+[i].toString()+","+[j].toString()+":"+
                        "<input type=\"number\" name:\"1,"+[i].toString()+","+[j].toString+"\">";
          /*        var namelabel = document.createElement('label');
                  namelabel.innerHTML = "Array "+i.toString()+" "+j.toString()
                  createform.appendChild(namelabel);
                  var inputelement = document.createElement('input');
                  inputelement.setAttribute("type", "number");
                  inputelement.setAttribute("name", "1"+i.toString()+j.toString())
                  createform.appendChild(inputelement);
            */
                }
             /*   var messagebreak= document.createElement('br');
                createform.appendChild(messagebreak)*/
                text+="<br>";
            }
        //alert("done");
//    text+="</form>"
  if(matnum == 2){
   text+="<button onclick=\"htmltoRender()\">Render</div>"
  }
    document.getElementById("inputform"+matnum.toString()).innerHTML = text;

    }

function both(){
  if(document.getElementById("1y").value == document.getElementById("2x").value){
  matrix(1);
  matrix(2);

  }
  else{
   alert("array 1y must equal 2x for matrix multiplication");
  }
}

var openFile = function(event) {
        var input = event.target;

        var reader = new FileReader();
        reader.onload = function(){
          var text = reader.result;
          var node = document.getElementById('output');
          node.innerText = matrixMultiplication(text);
          console.log(reader.result.substring(0, 200));
        };
        reader.readAsText(input.files[0]);
      };

function matrixMultiplication(text){
  //preprocessing
  var lines = text.split("\n");
  var rowlens= new Array(lines.length);
  for(i=0; i<lines.length; i++){
        var temp=lines[i].split(",")
        //alert(temp)
        //if line has no elements
        if(!temp[0]){
          rowlens[i]=0;
        }
        else{
          rowlens[i]=temp.length;
          if(i >=1 && rowlens[i-1] != 0 &&  rowlens[i-1] != temp.length){
           alert("uneven row lengths detected");
            return -1;
          }
    }
  }
  //more preprocessing
  //count amount of arrays and the row size of each
  var counter=0;
  var arry=[];
  for(i=0; i<= lines.length; i++){

    //reset counter, if in pre processing the row is 0 then there is a new array
    //if it is the last line, then count it only if the row it is not empty
    if(rowlens[i]==0 || (i== lines.length && rowlens[i]!=0)){
      arry.push(counter);
      counter=0;
    }
    else{
      counter++;
    }
  }
  if(arry.length >=1){
    //alert("The program detects: " + arry.length+" amount of arrays of row lengths: "+ arry.toString());
  }
  else{
    alert("The program detects: no arrays, refer to the guide on input");
    return 0;
  }

  //now that the data is safe
  //create amount of arrays
  listOfArrays=new Array(arry.length);
  for(i=0; i< arry.length;i++){
    listOfArrays[i]=[];
  }
  var arraycount=0;
  for(i=0; i<lines.length; i++){
        var temp=lines[i].split(",");

        //if line has no elements
        if(!temp[0]){
          arraycount++;
        }
        else{
          listOfArrays[arraycount].push(temp);
    }
  }
  //send list of arrays
  render(listOfArrays);
  return arry;
}
//https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_text
function render(listOfArrays){
      //alert(listOfArrays[0][0].length);
      var canvas = document.getElementById("input");
  if(listOfArrays[0].length!=listOfArrays[0][1].length){
    alert("Array 0 can not be multiplied by array 2");
  }
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");

       // ctx.fillStyle = "rgb(200,0,0)";
       // ctx.fillRect (10, 10, 55, 50);

       // ctx.fillStyle = "rgb(200, 0, 0)";
       // ctx.fillRect (70, 10, 55, 50);
        //draw each of the numbers
        for(i=0; i<2; i++){
          for(j=0; j<listOfArrays[i].length; j++){
            for(k=0; k<listOfArrays[i][j].length; k++){
              ctx.font = "50px serif";
              ctx.fillStyle = "rgb(200,200,200)";
              if(i==0){
              //ctx.fillRect (10+(k*60), 10+(j*60), 50, 50);
              ctx.fillText (listOfArrays[i][j][k].toString(), 10+(k*60), 50+(j*60));

              }
              else{
                //ctx.fillRect (10+(k*60)+(listOfArrays[i-1].length*60)+10, 10+(j*60) , 50, 50);
                ctx.fillText (listOfArrays[i][j][k].toString(), 10+(k*60)+((listOfArrays[i-1].length+1)*60), 50+(j*60));
              }
            }
          }
        }
         ctx.save()
         initNextState(ctx, listOfArrays);
      }

}
//animate the numbers
//https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations
function initNextState(ctx, listOfArrays){
  document.getElementById("requestnext").innerHTML="<button onclick=\"nextState()\">next state</div>";

}
function nextState(){

  // alert(state.toString());
  //use the state of the program to determine which part of the for loop it is on.
  //example: state 0, is initial state, so in matrix multiplication it is array1[0][0]* array2[0][0]
  //in state 1, if the length of the row is greater than one then array1[0][1]* array2[1][0]
  //in state of the col length of the second, then it will be array1[0][0]* array[0][1]
  //in state of the row length of the first times the col length of the second, then it will be array1[1][0] * array2[0][0]

  var ctx = document.getElementById("answer").getContext("2d");
  var canvas=document.getElementById("math");
   var ctx2 = canvas.getContext("2d");
  var rowx=(state/listOfArrays[0].length/listOfArrays[1][0].length)| 0;
  var coly=((state/listOfArrays[0][0].length) | 0) %(listOfArrays[1][0].length)
  //coly= coly%(listOfArrays[0].length*listOfArrays[1][0].length);
  var colx=state%listOfArrays[0][0].length;
  var resetcounter=state%listOfArrays[0].length;

  //alert("row x is : "+rowx.toString()+" col y is : "+ coly.toString()+" inner values are : "+ colx.toString());
//  alert("row x is : "+listOfArrays[0][rowx][colx].toString()+" col y is : "+ listOfArrays[1][colx][coly].toString());
  if(resetcounter == 0 && state !=0){

  /*
  alert(" col y is : "+ ((state/listOfArrays[0][0].length) | 0).toString()+
         "\nThe counter is : "+ (listOfArrays[0].length*listOfArrays[1][0].length).toString()+
         "\ncombined they are : "+(((state/listOfArrays[0][0].length) | 0)%(listOfArrays[0].length*listOfArrays[1][0].length)).toString()
        );
        */
    ctx.font = "50px serif";
  ctx.fillStyle = "rgb(200,200,200)";
    acc=0;

    if( coly==0 && rowx>=1){
      row=rowx-1;
      col=listOfArrays[1][0].length-1 ;
    }
    else{
      col=coly-1;
      row=rowx
    }


    for(var i=0;i<listOfArrays[0][0].length;i++){
    acc=acc+(parseInt(listOfArrays[0][row][i].replace(/\s+/g, ''))*
         parseInt(listOfArrays[1][i][col].replace(/\s+/g, '')));
      //alert("acc :"+ acc.toString());
    }
    ctx.fillText (acc.toString(), 10+(coly*60) , 10+(rowx+1)*60);
    ctx2.clearRect(0, 0, canvas.width, canvas.height);
  }
  if(((state/listOfArrays[0].length/listOfArrays[1][0].length)| 0) <= listOfArrays[0][0].length-1){
    ctx2.font = "50px serif";
    ctx2.fillStyle = "rgb(200,200,200)";
    ctx2.fillText (listOfArrays[0][rowx][colx].toString().replace(/\s+/g, '')+" * "+
                   listOfArrays[1][colx][coly].toString().replace(/\s+/g, ''), 10, 50+(resetcounter*60));


  state++;
  }
  else{
   alert ("Done!");
  }
}


//http://stackoverflow.com/questions/966225/how-can-i-create-a-two-dimensional-array-in-javascript
function createArray(length) {
    var arr = new Array(length || 0),
        i = length;

    if (arguments.length > 1) {
        var args = Array.prototype.slice.call(arguments, 1);
        while(i--) arr[length-1 - i] = createArray.apply(this, args);
    }

    return arr;
}
