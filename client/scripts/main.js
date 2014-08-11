$(document).ready(function() {
  var $result = $('#result');
  var $submitBtn = $('#submit');
  $('#form-direction').submit(function() {
      $result.html('');

      var message = $('#message').val();
      if (!message) {
        $result.html('Message cannot be empty.');
        return false;
      }

      var array = message.split(':');
      if (array.length !== 2 || !array[0] || !array[1]) {
        $result.html('Message must be in the format of Origin:destination');
        return false;
      }

      var action = $(this).attr('action');
      $submitBtn.attr('disabled','disabled');
      $.ajax({
          url: action,
          type: 'POST',
          data: JSON.stringify({
              message: message,
          }),
          // dataType: 'json',
          // contentType: 'application/json;charset=utf-8',
          success: function(data){
            console.log(data);
            $result.html('');
          },
          error: function(data) {
            console.log(data);
            $submitBtn.removeAttr('disabled');
            $result.html('Sorry, an error occurred. ' + data.response);
          }
      });
      return false;
  });
});
