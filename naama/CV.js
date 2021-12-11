var pics = ["../../lectures/img/2.jpg", "../../lectures/img/3.jpg", "../../lectures/img/4.jpg"];
var i = 0; 

function change_pic() {
    setTimeout(function() {
        document.getElementById("pic_animation").src = pics[i];
        i++;
        if(i < pics.length) {
            change_pic();
        } else {
            i = 0;
            change_pic();
        }
    }, 1000);
}

console.log("noy kasher")

function form_api() {
   var inputs = [document.getElementById("email"), document.getElementById("subject"), document.getElementById("textarea")];
   for (let i = 0; i < inputs.length; i++) {
       if (inputs[i].checkValidity()){
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
       }
   }
}

