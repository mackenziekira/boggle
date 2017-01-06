function populateList(data) {
  if (data) {
    $('#guessed-words').append('<li>' + data + '</li>');
}
}

function handleClick(evt) {
   if (evt.keyCode == 13) {
      word = this.value;
      $(this).val('');
      $.get('/guess', {guess : word }, populateList);
    }
}

$('#guess').on('keyup', handleClick);