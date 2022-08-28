function sendJSON(){ 
               
    let result = document.querySelector('#result'); 
    let intent = document.querySelector('#intent').value; 
    let label = document.querySelector('#label').value;    
    // Creating a XHR object 
    let xhr = new XMLHttpRequest(); 
    let url = "https://ml-models-api-kristianf89.herokuapp.com/spam_detection"; 
    //let url = "http://127.0.0.1:5000/spam_detection"; 


    let data_intent = {
        "sentence": intent
    };
    let options = {
      url: url,
      contentType:"application/json",
      type: "POST",
      data: JSON.stringify(data_intent),
        success: function( data, status, xhr ) {                       
          $('#result').html("<br><div class='alert alert-success' role='alert'>"+data.class+"</div>");
        },
        error: function( xhr, status, error ) {
            alert(error);
        }
    };
    $.ajax( options );
    } 

    function validation(){
      if(!$('#intent').val()){
          $('#result').html("<br><div class='alert alert-success' role='alert'>Please insert a text.</div>");
      }else{
          sendJSON();
      }
    }