function sendContact(name, email) {
  params = "name=" + name;
  send_url = "http://127.0.0.1:5000/contact/send_notification"; // url for calling send_to_notification
  var xhr = new XMLHttpRequest();
  xhr.open("POST", send_url, false); // false for syncronous requests
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(
    JSON.stringify({
      name: name, email: email
    }) // json data to send in the request
  );
  // httpGet(send_url + "?" + params);
  document.getElementById("peep").innerHTML =
    "Thanks " +
    name +
    " for contacting us, We'll get back to you as soon as possible"; //changing the content of text after submitting the details
}
