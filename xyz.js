var $form = $('form#test-form'),
    url = 'https://script.google.com/macros/s/AKfycbywIAvjvGp9OZ-wMn8WvL3n584CCliesDC2ARCROipjS6qQdMc/exec'

$('#submit-form').on('click', function(e) {
  e.preventDefault();
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serializeObject()
  }).success(
    // do something
  );
})
