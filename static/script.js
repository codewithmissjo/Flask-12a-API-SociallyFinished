$("#likeBtn").on("click", function(){
  // POST fetch
  fetch("/api/like",
    {
      method: "post",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      //make sure to serialize your JSON body
      body: JSON.stringify("1")
    }
  ).then( response => {
      console.log(response)
      // CALL THE NEW FUNCTION
      getLikes()
    }
  )
});

// THE NEW FUNCTION
function getLikes() {
  // GET fetch request
  fetch("/api/get/errything")
  .then( response => {
    console.log(response);
    return response.json();
  }).then(
    // update the HTML
    data => {
      $(".badge").html(data);
    }
  );
}
