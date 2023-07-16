function todayDate(){
    var d = new Date();
    var n = d.getFullYear() + "  ";
    return document.getElementById("date").innerHTML = n;
  }

todayDate()

setTimeout(function() {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 2000)
